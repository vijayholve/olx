from django.shortcuts import render, redirect
from .forms import PlanForm, PlanFeatureFormSet
from .models import Plan

def create_plan(request):
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        formset = PlanFeatureFormSet(request.POST)
        
        if plan_form.is_valid() and formset.is_valid():
            plan = plan_form.save()  # Save the Plan instance
            formset.instance = plan  # Associate formset with this plan
            
            formset.save()  # Save the PlanFeature instances
            return redirect('plan_list')  # Redirect to a list view or another page

    else:
        plan_form = PlanForm()
        formset = PlanFeatureFormSet()

    return render(request, 'create_plan.html', {
        'plan_form': plan_form,
        'formset': formset,
    })
