from django.shortcuts import render
from product.models import Product,ProductImage,User,State ,Plan,Transaction,Order,Customer
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


from django.db.models import Count, Sum
from datetime import datetime
import json

def sales_report(request):
    transactions = Transaction.objects.all()
    orders = Order.objects.all()
    
    # Aggregate sales data by month
    monthly_sales = (
        Order.objects
        .extra(select={'month': "EXTRACT(month FROM created_time)"})
        .values('month')
        .annotate(total_amount=Sum('amount'))
        .order_by('month')
    )


    monthly_data = {month: 0 for month in range(1, 13)}  # Dictionary with all months initialized to zero
    for entry in monthly_sales:
        monthly_data[int(entry['month'])] = float(entry['total_amount'])  # Fill with actual data

    # Prepare data for Chart.js
    labels = [datetime(2000, month, 1).strftime('%B') for month in range(1, 13)]  # Full month names
    data = [monthly_data[month] for month in range(1, 13)]  # Monthly totals with zero-filled months

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

    # context = {
    #     'chart_data': json.dumps(chart_data),
    # }
    

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
    
    Total_Orders=orders.count()
    
    context = {
        'all_states': all_states,
        'all_states_product_count': all_states_product_count,
            'products': products,
            'images': images,
            'users': users,
            "Total_Orders": Total_Orders,
        'transactions': transactions,
        'orders': orders,
        'chart_data': json.dumps(chart_data),
    
        }
    return render(request, 'panel/home_panel.html',context)