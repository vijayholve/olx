from django.shortcuts import render, redirect
from .form import PlanForm,FeaturesForm
from product.models import Plan,PlanFeature

def create_plan(request):
    if request.method == 'POST':
        # Initialize the forms
        plan_form = PlanForm(request.POST)
        features_form = FeaturesForm(request.POST)  # Create the features form
        
        if plan_form.is_valid() and features_form.is_valid():  # Check both forms
            plan = plan_form.save()  # Save the Plan
            selected_features = features_form.cleaned_data['features']  # Get selected features
            
            # Process the selected features
            for feature in selected_features:
                # Create or update the PlanFeature
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature
                )
            
            return redirect('plan-detail')  # Redirect after successful form submission
    
    else:
        plan_form = PlanForm()
        features_form = FeaturesForm()  # Initialize the feature form
        
    # Render the form in the template
    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
        'features_form': features_form
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