from django.urls import path
from . import views

urlpatterns = [
    path("plan-create",views.create_plan,name="plan-create"),
    path("plan-update",views.update_plan,name="plan-create"),

]

