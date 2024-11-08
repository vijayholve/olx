from django.shortcuts import render, redirect
from .form import PlanForm,FeaturesForm
from product.models import Plan,PlanFeature,Features

def create_plan(request):
    if request.method == 'POST':
        # Initialize the forms
        plan_form = PlanForm(request.POST)
        features_form = FeaturesForm(request.POST)
        
        if plan_form.is_valid() and features_form.is_valid():  # Check both forms
            plan = plan_form.save()  # Save the Plan
            selected_features = features_form.cleaned_data['features']  # Get selected features
            
            # Debugging: Check if selected features are correct
            print("Selected features:", selected_features)
            
            # Ensure features are added to the plan
            for feature in selected_features:
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                    included=True  
                    
                )
            selected_feature_ids = [feature.id for feature in selected_features]  # Extract IDs from selected features

# Now exclude the features by their IDs
            unselected_features = Features.objects.exclude(id__in=selected_feature_ids)
            for feature in unselected_features:
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                    included=False  
                    
                )
            
            return redirect('plan-detail')  # Redirect after successful form submission
        else:
            # If forms are not valid, print errors
            print("Plan Form Errors:", plan_form.errors)
            print("Features Form Errors:", features_form.errors)
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
        # Initialize the forms
        plan_form = PlanForm(request.POST, instance=)
        features_form = FeaturesForm(request.POST)
        
        if plan_form.is_valid() and features_form.is_valid():  # Check both forms
            plan = plan_form.save()  # Save the Plan
            selected_features = features_form.cleaned_data['features'] 
            
            # Debugging: Check if selected features are correct
            print("Selected features:", selected_features)
            
            # Ensure features are added to the plan
            for feature in selected_features:
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                    included=True  
                    
                )
            selected_feature_ids = [feature.id for feature in selected_features]  # Extract IDs from selected features

# Now exclude the features by their IDs
            unselected_features = Features.objects.exclude(id__in=selected_feature_ids)
            for feature in unselected_features:
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                    included=False  
                    
                )
            
            return redirect('plan-detail')  # Redirect after successful form submission
        else:
            # If forms are not valid, print errors
            print("Plan Form Errors:", plan_form.errors)
            print("Features Form Errors:", features_form.errors)
    else:
        plan_form = PlanForm()
        features_form = FeaturesForm() 
    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
        "features_form":features_form
    })

def delete_plan(request,plan_id):
    plan = Plan.objects.get(id=plan_id)
    plan.blocked = True
    plan.save()
    return redirect('plan-detail')