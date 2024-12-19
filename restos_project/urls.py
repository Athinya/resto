"""
URL configuration for restos_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import vies
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from others_apps.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from restos_app import views
from restos_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('BankDetails_tblfiltered/<str:cusid>/', BankDetails_tablfilteredView.as_view({'get': 'list'}), name='BankDetails_tblfilteredV'),   
    path('Shoplogo_tblFiltedata/<str:cusid>/', shoplogoFiltedataView.as_view({'get': 'list'}), name='Shoplogo_tblFiltedataV'),

    path('Amc/<str:cusid>/', Amc_tblView.as_view({'get': 'list'}), name='amc-cusid'),
    path('Settings_ProductCategory/<str:cusid>/', Settings_ProductCategoryView.as_view({'get': 'list'}), name='Settings_ProductCategory'),
    path('Settings_ProductDetailsSNo/<str:cusid>/', Settings_ProductDetailsSNoView.as_view({'get': 'list'}), name='Settings_ProductDetailsSNo'),
    path('Settings_ProductDetails/<str:cusid>/', Settings_ProductDetailsView.as_view({'get': 'list'}), name='Settings_ProductDetails'),   
    path('GstDetails/<str:cusid>/', GstDetailsView.as_view({'get': 'list'}), name='GstDetails'),
    path('StaffDetails/<str:cusid>/', StaffDetailsView.as_view({'get': 'list'}), name='StaffDetails'),   
    path('PaymentMethod/<str:cusid>/', PaymentMethodView.as_view({'get': 'list'}), name='PaymentMethod'),   
    path('PointSetting/<str:cusid>/', PointSettingView.as_view({'get': 'list'}), name='PointSetting'),   
    path('Settings_PrinterDetails/<str:cusid>/', Settings_PrinterDetailsView.as_view({'get': 'list'}), name='Settings_PrinterDetails'),   
    path('Settings_Combo/<str:cusid>/', Settings_ComboView.as_view({'get': 'list'}), name='Settings_Combo'),   
    path('PointSetting/<str:cusid>/', PointSettingView.as_view({'get': 'list'}), name='PointSetting'),   
    path('Sales_IncomeDetailsdatewise/<str:cusid>/<str:dt>/', Sales_IncomeDetailsdatewiseView.as_view({'get': 'list'}), name='Sales_IncomeDetailsdatewise'),   
    path('Settings_Role/<str:cusid>/', Settings_RoleView.as_view({'get': 'list'}), name='Settings_Role'),   
    path('Settings_Password/<str:cusid>/', Settings_PasswordView.as_view({'get': 'list'}), name='Settings_Password'),   
    path('Settings_usermanagement/<str:cusid>/', Settings_usermanagementView.as_view({'get': 'list'}), name='Settings_usermanagement'),   


    path('DashboardTodayRecordsView/<str:cusid>/', DashboardTodayRecordsView.as_view({'get': 'list'}), name='DashboardTodayRecordsView'),
    path('DashboardWeeklyRecords/<str:cusid>/', DashboardWeeklyRecordsView.as_view({'get': 'list'}), name='DashboardWeeklyRecordsView'),
    path('DashboardOrderSalesDetails/<str:cusid>/', DashboardOrderSalesDetailsView.as_view({'get': 'list'}), name='DashboardOrderSalesDetails'),
    path('DashboardTopSelling/<str:cusid>/', DashboardTopSellingView.as_view({'get': 'list'}), name='DashboardTopSellingView'),

    path('SalesCustomer/<str:cusid>/', SalesCustomerView.as_view({'get': 'list'}), name='SalesCustomer'),   
    path('SalesPaymentSno/<str:cusid>/', SalesPaymentSnoView.as_view({'get': 'list'}), name='SalesPaymentSno'),   
    path('SalesPaymentRoundDetails/<str:cusid>/', SalesPaymentRoundDetailsView.as_view({'get': 'list'}), name='SalesPaymentRoundDetails'),   
    path('SalesPaymentDetaied/<str:cusid>/', SalesPaymentDetaiedView.as_view({'get': 'list'}), name='SalesPaymentDetaied'),   
    path('Sales_tableCount/<str:cusid>/', Sales_tableCountView.as_view({'get': 'list'}), name='Sales_tableCount'),   
    path('Sales_serialno/<str:cusid>/', Sales_serialnoView.as_view({'get': 'list'}), name='Sales_serialno'),   
    path('SalesRoundAndDetails/<str:cusid>/', SalesRoundDetails_View.as_view({'get': 'list'}), name='Sales_Details_Round_tbl'), 
    path('EditSalesreports/<str:cusid>/<str:dt>/<str:billno>/', EditSalesreportsView.as_view({'get': 'list'}), name='EditSalesreports'),
 
    path('Purchase_serialNo/<str:cusid>/', Purchase_serialNoView.as_view({'get': 'list'}), name='Purchase_serialNo'),
    path('PurchaseProductCategory/<str:cusid>/', PurchaseProductCategoryView.as_view({'get': 'list'}), name='PurchaseProductCategory'),   
    path('PurchaseProductDetails/<str:cusid>/', PurchaseProductDetailsView.as_view({'get': 'list'}), name='PurchaseProductDetails'),
    path('PurchasePaymentSNo/<str:cusid>/', PurchasePaymentSNoView.as_view({'get': 'list'}), name='PurchasePaymentSNo'),   
    path('PurchasePayments/<str:cusid>/', PurchasePaymentsView.as_view({'get': 'list'}), name='PurchasePayments'),   
    path('PurchaseSupplierNames/<str:cusid>/', PurchaseSupplierNamesView.as_view({'get': 'list'}), name='PurchaseSupplierNames'),   
    path('PurchaseRoundDetails/<str:cusid>/', PurchaseRoundDetails_View.as_view({'get': 'list'}), name='PurchaseRoundDetails'),   
    path('EditPurchasereportsView/<str:cusid>/<str:date>/<str:serialno>/', EditPurchasereportsView.as_view({'get': 'list'}), name='EditPurchasereportsView'),
  
    path('Order_Sno/<str:cusid>/', Order_Sno_View.as_view({'get': 'list'}), name='Order_Sno'),         
    path('OrderPayment/<str:cusid>/', OrderPayment_View.as_view({'get': 'list'}), name='OrderPayment'),   
    path('OrderSalesRoundDetails/<str:cusid>/', OrderSalesRoundDetails_View.as_view({'get': 'list'}), name='OrderSalesRoundDetails'),   
    path('EditOrderSales/<str:cusid>/<str:billno>/<str:dt>', EditOrderSalesView.as_view({'get': 'list'}), name='OrderSalesRoundDetails'),   
   
    path('Vendor_Sno/<str:cusid>/', Vendor_Sno_View.as_view({'get': 'list'}), name='Vendor_Sno'),   
    path('VendorsName/<str:cusid>/', VendorsNameView.as_view({'get': 'list'}), name='VendorsName'),   
    path('SalesFetchVendorPaymentcusid/<str:cusid>/', SalesFetchVendorPaymentcusidView.as_view({'get': 'list'}), name='SalesFetchVendorPaymentcusid'),   
     


    path('Wastage_serialno/<str:cusid>/', Wastage_serialno_view.as_view({'get': 'list'}), name='Wastage_serialno'),   
    path('Wastage_Details_Round/<str:cusid>/', Wastage_Details_Round_view.as_view({'get': 'list'}), name='Wastage_Details_Round'),   
   
    path('Stock_Sno/<str:cusid>/', Stock_Sno_View.as_view({'get': 'list'}), name='Stock_Sno'),   
    path('Stock_Details_Round/<str:cusid>/', Stock_Details_Round_View.as_view({'get': 'list'}), name='Stock_Details_Round'),   
   
    path('Usageserialno/<str:cusid>/', Usageserialno_View.as_view({'get': 'list'}), name='Usageserialno'),   
    path('UsageRound_Details/<str:cusid>/', UsageRound_Details_View.as_view({'get': 'list'}), name='UsageRound_Details'),   
   
    path('IncomeEntryDetail/<str:cusid>/', IncomeEntryDetailView.as_view({'get': 'list'}), name='IncomeEntryDetail'),   
    path('ExpenseCat/<str:cusid>/', ExpenseCatView.as_view({'get': 'list'}), name='ExpenseCat'),   
    path('ExpenseEntryDetail/<str:cusid>/', ExpenseEntryDetailView.as_view({'get': 'list'}), name='ExpenseEntryDetail'),   
      
    path('SalesGraphCharts/<str:cusid>/', SalesGraphView.as_view({'get': 'list'}), name='SalesGraph'),   

    path('DatewiseSalesReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseSalesReportView.as_view({'get': 'list'}), name='Datewise_Sales_reports'),
    path('DaySelectedSales/<str:cusid>/<str:dt>/', TodaySalesReportView.as_view({'get': 'list'}), name='DaySelected_Sales'),
    path('CusnamewiseSalesReport/<str:cusid>/<str:cusname>/', CusnamewiseSalesReportView.as_view({'get': 'list'}), name='cusnamewise_sales_reports'),
    path('CusnamewiseSalesPaymentReport/<str:cusid>/<str:name>/', CusnamewiseSalesPaymentReportView.as_view({'get': 'list'}), name='CusnamewiseSales_PaymentReport'),
    path('SalesLeadge/<str:cusid>/<str:start_dt>/', Sales_Leadge_overall_repots.as_view({'get': 'list'}), name='SalesLeadge'),
    path('DatewiseOrderSalesReport/<str:cusid>/<str:start_dt>/<str:end_dt>/',DatewiseOrderSalesReportView.as_view({'get': 'list'}), name='DatewiseOrderSalesReport'),
    path('DeliveryDatewiseOrderSalesReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DeliveryDatewiseOrderSalesReportView.as_view({'get': 'list'}), name='DeliveryDatewiseOrderSalesReport'),
    path('DatewiseVendorSalesReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseVendorSalesReportView.as_view({'get': 'list'}), name='DatewiseVendorSalesReport'),
    path('DatewisePurchaseReport/<str:cusid>/<str:start_date>/<str:end_date>/', DatewisePurchaseReportView.as_view({'get': 'list'}), name='Datewise_Purchase_reports'),
    path('AgentwiseSalesReport/<str:cusid>/<str:purchasername>/', AgentwisePurchaseReportView.as_view({'get': 'list'}), name='Agentwise_sales_reports'),
    path('AgentwiseSalesPaymentReport/<str:cusid>/<str:agentname>/', AgentwisePurchasePaymentReportView.as_view({'get': 'list'}), name='Agentwise_sales_reports'),
    path('PurchaseLeadge/<str:cusid>/<str:start_date>/', Purchase_Leadge_overall_repots.as_view({'get': 'list'}), name='PurchaseLeadge'),
    path('DateWiseStockOverAllReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseStockReportView.as_view({'get': 'list'}), name='DateWiseStockOverAllReport'),
    path('DateWiseWastageReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseWastageReportView.as_view({'get': 'list'}), name='DateWiseWastageReport'),
    path('DatewiseKitchenUsageReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseKitchenUsageReportView.as_view({'get': 'list'}), name='DatewiseKitchenUsageReport'),
    path('DateWiseIncomeReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseIncomeReportView.as_view({'get': 'list'}), name='DateWiseIncomeReport'),
    path('DateWiseExpenseReport/<str:cusid>/<str:start_dt>/<str:end_dt>/', DatewiseExpenseReportView.as_view({'get': 'list'}), name='DateWiseExpenseReport'),
    re_path(
        r'^sales_printer/(?P<cusid>[^/]*)/(?P<restaurant_name>[^/]*)/(?P<area>[^/]*)/(?P<area2>[^/]*)/(?P<city>[^/]*)/(?P<gstno>[^/]*)/(?P<fssai>[^/]*)/(?P<contact>[^/]*)/(?P<bill_no>[^/]*)/(?P<bill_id>[^/]*)/(?P<pay_type>[^/]*)/(?P<date>[^/]*)/(?P<bill_time>[^/]*)/(?P<customer_name>[^/]*)/(?P<customer_contact>[^/]*)/(?P<table_No>[^/]*)/(?P<servent>[^/]*)/(?P<products_param>[^/]*)/(?P<total_item>[^/]*)/(?P<totalamt>[^/]*)/(?P<total_qty>[^/]*)/(?P<total_dis>[^/]*)/(?P<sgstper25>[^/]*)/(?P<sgstper6>[^/]*)/(?P<sgstper9>[^/]*)/(?P<sgstper14>[^/]*)/(?P<final_amt>[^/]*)/$',
        views.sales_printer,
        name='sales_printer'
    ),
    
    re_path(
    r'^order_sales/(?P<cusid>[^/]*)/(?P<restaurant_name>[^/]*)/(?P<area>[^/]*)/(?P<area2>[^/]*)/(?P<city>[^/]*)/(?P<gstno>[^/]*)/(?P<fssai>[^/]*)/(?P<contact>[^/]*)/(?P<bill_no>[^/]*)/(?P<bill_id>[^/]*)/(?P<pay_type>[^/]*)/(?P<date>[^/]*)/(?P<bill_time>[^/]*)/(?P<customer_name>[^/]*)/(?P<customer_contact>[^/]*)/(?P<products_param>[^/]*)/(?P<total_item>[^/]*)/(?P<totalamt>[^/]*)/(?P<total_qty>[^/]*)/(?P<total_dis>[^/]*)/(?P<sgstper25>[^/]*)/(?P<sgstper6>[^/]*)/(?P<sgstper9>[^/]*)/(?P<sgstper14>[^/]*)/(?P<final_amt>[^/]*)/(?P<delivery>[^/]*)/(?P<paid_amt>[^/]*)/(?P<balance_amt>[^/]*)/(?P<order_sales>[^/]*)/$',
    views.order_sales,
    name='order_sales'
    ),
    re_path(
        r'^Kitechan_print/(?P<header>[^/]+)/(?P<Table_no>[^/]+)/(?P<date>[^/]+)/(?P<time>[^/]+)/(?P<sname>[^/]+)/(?P<products_param>.*)/(?P<cusid>[^/]+)/$',
        views.Kitechan_print,
        name='Kitechan_print'
    ),
    re_path('BR/<str:details>/',views.barcode_form, name='barcode_form'), 
    path('QR/<str:details>/', views.Qrcode_form, name='barcode_form'),
    path(
        'Daily_report/<str:restaurant_name>/<str:date>/<path:items>/',  # Capture restaurant_name, date, and items
        views.Daily_report,
        name='Daily_report'
    ),
        re_path(
    r'^Stock_added/(?P<cusid>[^/]*)/(?P<restaurant_name>[^/]*)/(?P<bill_no>[^/]*)/(?P<bill_id>[^/]*)/(?P<pay_type>[^/]*)/(?P<date>[^/]*)/(?P<bill_time>[^/]*)/(?P<products_param>[^/]*)/(?P<total_item>[^/]*)/(?P<order_sales>[^/]*)/$',
    views.Stock_added,
    name='Stock_added'
   ),

   
   
    path('SalesPaymentView/', SalesPaymentRoundDetailsView.as_view({'get': 'list'}), name='salespayment_reports'),
    path('test-cors/', test_cors),

    path('',include('restos_app.urls')),
]
