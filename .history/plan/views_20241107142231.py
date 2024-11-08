from django.shortcuts import render, redirect
from .form import PlanForm,PlanFeaturesForm
from product.models import Plan

def create_plan(request):
    if request.method == 'POST':
        plan_form = PlanForm(request.POST)
        
        if plan_form.is_valid():
            plan = plan_form.save()
            selected_features = features_form.cleaned_data['features']
            for feature in selected_features:
                # Create or update PlanFeature
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                    defaults={'included': True}
                )           
            return redirect('plan-detail')  
           
    else:
        plan_form = PlanForm()
        features_form = PlanFeaturesForm()

    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
    })

def update_plan(request,plan_id):
    plan=Plan.objects.get(id=plan_id)
    if request.method == 'POST':
        plan_form = PlanForm(request.POST, instance=plan)
        
        if plan_form.is_valid():
            plan = plan_form.save()           
            return redirect('plan-detail')  
    else:
        plan_form = PlanForm(instance=plan)

    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
    })

def delete_plan(request,plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.blocked = True
    plan.save()
    return redirect('plan-detail')