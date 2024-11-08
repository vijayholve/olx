from django.shortcuts import render, redirect
from .form import PlanForm, PlanFeatureFormSet
from product.models import Plan

def plan_detail(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    # Get the features related to the plan
    plan_features = PlanFeature.objects.filter(plan=plan)

    if request.method == 'POST':
        formset = PlanFeatureFormSet(request.POST, instance=plan)
        if formset.is_valid():
            formset.save()
    else:
        formset = PlanFeatureFormSet(instance=plan)

    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
        'formset': formset,
    })
