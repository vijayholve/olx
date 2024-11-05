from django.shortcuts import render
from product.models import Product,ProductImage,User,State ,Plan,Transaction,Order
from django.db.models import Count
from django.db.models import Sum
import json
def admin_panel(request):
    if request.user.is_authenticated and request.user.is_staff:
        products = Product.objects.all()
        images = ProductImage.objects.all()
        users = User.objects.all()
        states_with_product_count = State.objects.annotate(product_count=Count('product')).values('name', 'product_count')

    # Prepare the labels and data lists
        all_states = []
        all_states_product_count = []

        for state in states_with_product_count:
            all_states.append(state['name'])
            all_states_product_count.append(state['product_count'])
        
        context = {
            'all_states': all_states,
            'all_states_product_count': all_states_product_count,
                'products': products,
                'images': images,
                'users': users,
            }
        return render(request, 'panel/admin_panel.html', context)




def plan_list(request):
    plans = Plan.objects.prefetch_related('planfeature_set__feature').all()
    return render(request, 'panel/plan_details.html', {'plans': plans})


def sales_report(request):
    # Fetch all transactions and orders
    transactions = Transaction.objects.all()
    orders = Order.objects.all()
    
    # Aggregate sales data for the histogram (e.g., total amounts per month)
    monthly_sales = (
        Order.objects
        .extra(select={'month': "EXTRACT(month FROM created_time)"})
        .values('month')
        .annotate(total_amount=Sum('amount'))
        .order_by('month')
    )

    # Prepare data for Chart.js, converting Decimal to float
    labels = [f"Month {int(entry['month'])}" for entry in monthly_sales]
    data = [float(entry['total_amount']) for entry in monthly_sales]  # Convert Decimal to float

    # Convert data to JSON format for Chart.js
    chart_data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Total Sales',
                'data': data,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1,
            }
        ]
    }
    products = Product.objects.all()
    images = ProductImage.objects.all()
    users = User.objects.all()
    states_with_product_count = State.objects.annotate(product_count=Count('product')).values('name', 'product_count')

# Prepare the labels and data lists
    all_states = []
    all_states_product_count = []

    for state in states_with_product_count:
        all_states.append(state['name'])
        all_states_product_count.append(state['product_count'])
    
    context = {
        'all_states': all_states,
        'all_states_product_count': all_states_product_count,
            'products': products,
            'images': images,
            'users': users,
        }
    return render(request, 'panel/home_panel.html',co)