from django.urls import path
from . import views

urlpatterns = [
    path("plan-create",views.create_plan,name="plan-create"),
    path("plan-update",views_plan,name="plan-create"),

]

