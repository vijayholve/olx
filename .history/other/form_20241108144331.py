from django import forms
from product.models import State, Category, Features, PaymentType, Transaction, Order

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

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['Customer', 'transaction_no', 'amount', 'plan', 'payment_type']

model = Order