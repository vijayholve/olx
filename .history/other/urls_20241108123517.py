from django.urls import path
from . import views

urlpatterns = [
        path('details_state/', views.state_details, name='details_state'),
    path('create_state/', views.create_state, name='create_state'),
    path('update_state/<str:pk>/', views.update_state, name='update_state'),
    path('delete_state/<str:pk>/', views.delete_state, name='delete_state'),
    path('details_category/', views.category_details, name='details_category'),
    path('/', views.create_state, name='create_state'),
    path('update_state/<str:pk>/', views.update_state, name='update_state'),
    path('delete_state/<str:pk>/', views.delete_state, name='delete_state'),
]
