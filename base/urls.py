from django.urls import path 
from . import views

urlpatterns = [
    path('login-page/',views.login_page,name="login-page"),
    path("register-page/",views.customeze_register_page,name="register-page"),
    path("logout-page/",views.login_page,name="logout-page"),
        path('customer-profile/<str:id>/',views.user_profile,name='customer-profile'),
    path('customer-update/<str:c_id>/',views.update_customer_details,name='customer-update'),
    path('customer-delete/<str:c_id>/',views.delete_customer_details,name='customer-delete'),

]
