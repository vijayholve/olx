from django.urls import path 
from . import views

urlpatterns = [
    path('login-page/',views.login_page,name="login-page"),
    path("register-page/",views.re),
]
