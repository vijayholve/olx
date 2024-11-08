from django import forms
from product.models import State, Category, Features, PaymentType, Order

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ['name']

class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['name']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['plan', 'payment_type', 'customer', 'amount', 'payment_status']order_no
transaction_no
plan
payment_type
customer
amount
payment_status