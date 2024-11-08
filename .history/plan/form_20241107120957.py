from django import forms
from django.forms import modelformset_factory, inlineformset_factory
from product.models import Plan, Features, PlanFeature

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'plan_type', 'price', 'blocked']

class PlanFeatureForm(forms.ModelForm):
    class Meta:
        model = PlanFeature
        fields = ['feature', 'included', 'blocked']

    def __init__(self, *args, **kwargs):
        super(PlanFeatureForm, self).__init__(*args, **kwargs)
        self.fields['feature'].queryset = Features.objects.filter(blocked=False)  # Filter blocked features out
PlanFeatureFormSet = inlineformset_factory(
    Plan, PlanFeature, fields=('feature', 'included'), extra=1, can_delete=True
)