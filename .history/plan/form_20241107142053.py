from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from product.models import Plan, Features, PlanFeature

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'plan_type', 'price']

class PlanFeatureForm(forms.ModelForm):
    class Meta:
        model = PlanFeature
        fields = ['feature', 'included']

    def __init__(self, *args, **kwargs):
        super(PlanFeatureForm, self).__init__(*args, **kwargs)
        self.fields['feature'].queryset = Features.objects.filter(blocked=False)  # Filter blocked features out
        
        
class PlanFeaturesForm(forms.Form):
    features = forms.ModelMultipleChoiceField(
        queryset=Feature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )