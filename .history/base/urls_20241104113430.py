from django.urls import path 
from . import views

urlpatterns = [
    path('login-page/',views.lo),
]