from django.shortcuts import render, redirect
from .form import PlanForm, PlanFeatureFormSet
from product.models import Plan

def create_plan(request):
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        
        if plan_form.is_valid():
            plan = plan_form.save()           
            formset.save()  #
            return redirect('plan-detail')  # Redirect to a list view or another page

    else:
        plan_form = PlanForm()

    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
    })
