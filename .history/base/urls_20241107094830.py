from django.urls import path 
from . import views

urlpatterns = [
    path('login-page/',views.login_page,name="login-page"),
    path("register-page/",views.customeze_register_page,name="register-page"),
    path("logout-page/",views.login_page,name="logout-page"),
    path('user-update/',views.login_page,name="login-page')

    
]
