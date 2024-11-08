from django.urls import path
from . import views

urlpatterns = [
        path('details_state/', views.state_details, name='details_state'),
    path('create_state/', views.create_state, name='create_state'),

]
