from django import forms
from product.models import Plan, Features

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'plan_type', 'price']

class FeaturesForm(forms.Form):
    features = forms.ModelMultipleChoiceField(
        queryset=Features.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'name': 'features'}),
        required=True,
    )

