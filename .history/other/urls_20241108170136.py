from django.urls import path
from . import views

urlpatterns = [
        path('details_state/', views.state_details, name='details_state'),
    path('create_state/', views.create_state, name='create_state'),
    path('update_state/<str:pk>/', views.update_state, name='update_state'),
    path('delete_state/<str:pk>/', views.delete_state, name='delete_state'),
    path('details_category/', views.category_details, name='details_category'),
    path('create_category/', views.create_category, name='create_category'),
    path('update_category/<str:pk>/', views.update_category, name='update_category'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete_category'),
    path('details_order/', views.order_details, name='details_order'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),
    path('details_paymentType/', views.paymentType_details, name='details_paymentType'),
    path('create_paymentType/', views.create_paymentType, name='create_paymentType'),
    path('update_paymentType/<int:pk>/', views.update_paymentType, name='update_paymentType'),
    path('delete_paymentType/<str:pk>/', views.delete_paymentType, name='delete_paymentType'),
    
    path('details_order/', views.order_details, name='details_order'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<str:pk>/', views.delete_order, name='delete_paymentType'),
    
]
