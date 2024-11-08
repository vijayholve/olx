from django.urls import path
from . import views

urlpatterns = [
        path('create_state/', views.create_state, name='create_state'),
    path('create_state/', views.create_state, name='create_state'),
    # Add other paths for the different forms
]
