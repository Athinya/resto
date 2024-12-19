# Use an official Python runtime as a parent image
FROM python:3.12-slim AS build

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ACCEPT_EULA=Y

# Set the working directory inside the container
WORKDIR /app

# Install necessary system dependencies for MSSQL and cleanup
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    apt-transport-https \
    gnupg2 \
    build-essential \
    unixodbc-dev \
    ca-certificates && \
    # Retrieve the Microsoft GPG key
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft.gpg && \
    # Add the Microsoft repository to sources
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/debian/10/prod/ buster main" > /etc/apt/sources.list.d/mssql-release.list && \
    # Update package list
    apt-get update && \
    # Install msodbcsql17 package
    apt-get install -y msodbcsql17 && \
    # Clean up unnecessary files to reduce the image size
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python dependencies in one layer
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the current directory contents into the container at /app
COPY . /app/

# Build the runtime image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ACCEPT_EULA=Y

# Set the working directory inside the container
WORKDIR /app

# Install only runtime dependencies (necessary for running the app)
RUN apt-get update && apt-get install -y --no-install-recommends unixodbc && \
    # Print logs to help diagnose the error
    apt-get -y install --no-install-recommends unixodbc || echo "Failed to install unixodbc" && \
    # Clean apt cache
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the dependencies and the application from the build stage
COPY --from=build /app /app

# Collect static files (optional, if you have static files)
RUN python manage.py collectstatic --noinput || echo "No static files to collect"

# Expose the port that the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "restos_project.wsgi:application"]
