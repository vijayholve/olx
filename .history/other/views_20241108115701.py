from django.shortcuts import render,redirect
from .form import StateForm, CategoryForm, FeaturesForm, PaymentTypeForm, TransactionForm, OrderForm
from django.contrib.auth.decorators import login_required
from product.models import Product,State
@login_required(login_url="login-page")
def state_details(request):
    states = State.objects.filter(blocked=False)
    return render(request, 'other/state_details.html', {'states': states})

@login_required(login_url="login-page")
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
    return render(request, 'create_state.html', {'form': form,
                                                 "operation": operation,
                                                 "title": title}
                  )

# Create your views here.
