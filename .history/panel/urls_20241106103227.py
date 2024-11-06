from django.urls import path
from . import views 

urlpatterns = [
    path('admin-panel/',views.admin_panel,name="admin-panel"),
    path('plan-detail/',views.plan_list,name="plan-detail"),
        path('sales-report/', views.sales_report, name='sales_report'),
        path('customer-details/',views.customer_details, name='customer-detail)
]

