from django import forms
from .models import Plan, Feature, PlanFeature

class PlanFeatureForm(forms.ModelForm):
    class Meta:
        model = PlanFeature
        fields = ['feature', 'included']

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'price']

class PlanFeaturesForm(forms.Form):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )