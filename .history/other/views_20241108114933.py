from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, TransactionForm, OrderForm

def create_state(request):
    operation="create"
    title="State"
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = StateForm()
    return render(request, 'create_state.html', {'form': form
                                                 "operation":})

# Create your views here.
