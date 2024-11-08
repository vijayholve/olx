from django.urls import path
from . import views

urlpatterns = [
    path("plan-create",views.create_plan,name="plan-create"),
    path("plan-update/<str:plan_id>/",views.update_plan,name="plan-update"),
        path("plan-delete/<str:plan_id>/",views.delete_plan,name="plan-delete"),

]

