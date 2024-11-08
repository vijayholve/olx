
Here's how you can structure the logic for the form submission in Django views. It handles both the PlanForm and FeaturesForm logic, saving the selected features for the created plan.

views.py Logic:
python
Copy code
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PlanForm, FeaturesForm
from .models import Plan, Feature, PlanFeature

def create_plan(request):
    if request.method == 'POST':
        # Instantiate the forms with the POST data
        plan_form = PlanForm(request.POST)
        features_form = FeaturesForm(request.POST)
        
        if plan_form.is_valid() and features_form.is_valid():
            # Save the plan form
            plan = plan_form.save()

            # Get the selected features from the form
            selected_features = features_form.cleaned_data['features']  # List of selected features
            
            # Add selected features to the plan
            for feature in selected_features:
                # You can use update_or_create to prevent duplicates
                PlanFeature.objects.update_or_create(
                    plan=plan,
                    feature=feature,
                )
            
            return redirect('plan_success')  # Redirect to a success page after saving

    else:
        # If the request is GET, instantiate the forms without POST data
        plan_form = PlanForm()
        features_form = FeaturesForm()

    return render(request, 'plan/create_plan.html', {
        'plan_form': plan_form,
        'features_form': features_form
    })
Explanation:
Form Handling:

If the method is POST, the PlanForm and FeaturesForm are instantiated with the submitted data (request.POST).
Both forms are validated with form.is_valid().
Saving Plan:

If the PlanForm is valid, we save the plan instance with plan_form.save(). This will save the plan data (like plan name, type, and price) into the database.
Saving Features:

The features_form.cleaned_data['features'] will give us the list of selected features.
We iterate over the selected features and use PlanFeature.objects.update_or_create() to add them to the PlanFeature model. This avoids duplicate entries for the same plan-feature combination.
Redirecting:

After saving the plan and its features, we redirect the user to a success page (plan_success). You can change this to any URL you want.
GET Request:

When the page is accessed via a GET request (for the first time or after validation errors), the empty forms are displayed.
Forms (for context):
forms.py (PlanForm and FeaturesForm):
python
Copy code
from django import forms
from .models import Plan, Feature

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'plan_type', 'price']

class FeaturesForm(forms.Form):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )