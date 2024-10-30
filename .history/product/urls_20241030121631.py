from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-product/', views.product_create_form, name='product_create_form'), 
    path('create-product/',views.product_details),
]