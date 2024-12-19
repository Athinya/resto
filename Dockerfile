# Use a Debian-based Python image
FROM python:3.10-slim

# Set environment variables to avoid issues with Python bytecode and buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies required for your project
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unixodbc-dev \
    gnupg \
    ca-certificates && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    unixodbc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements and install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "employee_project.wsgi:application", "--bind", "0.0.0.0:8000"]
