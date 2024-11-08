from django.urls import path 
from . import views

urlpatterns = [
    path('login-page/',views.login_page,name="login-page"),
    path("register-page/",views.customeze_register_page,name="register-page"),
    path("logout-page/",views.login_page,name="logout-page"),
    path('customer-create/<str:c_id>/',views.create_customer_details,name='customer-update'),
    path('customer-update/<str:c_id>/',views.update_customer_details,name='customer-update'),

]
