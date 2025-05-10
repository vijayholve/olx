from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-product/', views.product_create_form, name='product_create_form'), 
    path('details-product/<str:product_id>',views.product_details,name='product_details'),
    path('update-product/<str:product_id>/',views.product_update_form, name='product-update'),
    path('delete-product/<str:product_id>/',views.product_delete, name='product-delete'),
path('payment-product/<int:product_id>/', views.CreatePaymentView.as_view(), name='payment-product'),

] 