from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage, ProductOrder,State  ,Category
from django import template 

from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from itertools import zip_longest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import razorpay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import logging
register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, ProductImage  # Import your models
@login_required(login_url='login-page')
def home(request):
    category = request.GET.get('category', '')
    query = request.GET.get('search', '')
    condition=request.GET.get('condition', '')
    
    context1={}
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(category__name__icontains=query)
        )


    elif category:
        products = Product.objects.filter(category__name=category)
        context1['category'] = category
    elif condition:
        products = Product.objects.filter(condition=condition)
        context1['condition'] = condition
    else:
        products = Product.objects.filter(blocked=False)

    productimage = {}
    for product in products:
        if image := ProductImage.objects.filter(product=product).first():
            productimage[product.id] = image.image  
    all_category = Category.objects.filter(blocked=False)
    context = {
        'products': products,
        'productimage': productimage,
        'all_category': all_category,
        'query': query,  
    }
    context.update(context1)
    return render(request, "product/home.html", context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductForm, MultipleImagesForm
from .models import ProductImage

@login_required(login_url='login-page')
def product_create_form(request):
    number_of_image_fields = 4

    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = MultipleImagesForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save(commit=False)
            product.posted_by = request.user
            product.save()

            # Handle multiple images
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('home')
    else:
        product_form = ProductForm()
        image_form = MultipleImagesForm()

    context = {
        'number_of_image_fields': range(number_of_image_fields),
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'product/create_product.html', context)


@login_required(login_url='login-page')
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    suggested_products = Product.objects.all().exclude(id=product.id, blocked=False,category__blocked=False)[:9]  # Fetch up to 9 suggested products
    first_image=ProductImage.objects.filter(product=product).first()
    grouped_suggested_products = [
        list(filter(None, group)) for group in zip_longest(*[iter(suggested_products)]*4)
    ]
    product_images_all=[]
    for pro_img in ProductImage.objects.filter(product=product):
        product_images_all += pro_img.image.url  
    suggest_product_images = {
        suggested_product.id: ProductImage.objects.filter(product=suggested_product).first().image.url 
        if ProductImage.objects.filter(product=suggested_product).exists() else None
        for suggested_product in suggested_products
    }

    context = {
        'product': product,
        'suggested_products': suggested_products,
        'suggest_product_images': suggest_product_images,
        "product_images_all":product_images_all,
        'grouped_suggested_products': grouped_suggested_products,
        "first_image":first_image

    }
    
    return render(request, 'product/product_details.html', context)


@login_required(login_url='login-page')
def product_update_form(request, product_id):
    # Fetch the existing product
    product = get_object_or_404(Product, id=product_id)

    # Number of image fields you want to display in the form
    number_of_image_fields = 4

    # Check if the request is POST
    if request.method == 'POST':
        # Create form instances for product and images
        product_form = ProductForm(request.POST, instance=product)
        image_form = MultipleImagesForm(request.FILES)

        # Check if the forms are valid
        if product_form.is_valid() or image_form.is_valid():
            # Save the product form
            product = product_form.save(commit=False)
            product.posted_by = request.user  # Ensure the user is the same
            product.save()

            # Handle images
            # Delete existing images if any
            if 'images' in request.FILES:
                # Clear existing images related to the product
                for pro_img in ProductImage.objects.filter(product=product) :
                    # product.productimage_set.all().delete()
                    pro_img.delete()

                # Add new images
                images = request.FILES.getlist('images')
                for img in images:
                    ProductImage.objects.create(product=product, image=img)

            return redirect('product-all-details')  # Redirect to the home page or product list

    else:
        # Prepopulate the form with existing product data
        product_form = ProductForm(instance=product)
        image_form = MultipleImagesForm()

    context = {
        'number_of_image_fields': range(number_of_image_fields),  # Pass the range as context
        'product_form': product_form,
        'image_form': image_form,
        'product': product  # Pass the product to the template for editing
    }

    return render(request, 'product/product_update.html', context)
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.blocked=True
    product.save()  
    return redirect('product-all-details') 


logger = logging.getLogger(__name__)
client=  razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@method_decorator(csrf_exempt, name='dispatch')
class CreatePaymentView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        try:
            logger.info("Fetching product with id: %s", product_id)
            product = get_object_or_404(Product, id=product_id)

            if not product.price:
                raise ValueError("Product price is missing or invalid.")

            order_data = {
                'amount': int(product.price * 100),
                'currency': 'INR',
                'payment_capture': '1',
            }

            # Check Razorpay client is configured
            logger.info("Creating Razorpay order")
            razorpay_order = client.order.create(data=order_data)

            productOrder = ProductOrder.objects.create(
                product=product,
                customer=request.user,
                amount=product.price,
                razorpay_id=razorpay_order['id'],
            )

            logger.info("Payment created successfully")

            return JsonResponse({
                "order_id": razorpay_order['id'],
                "razorpay_key_id": settings.RAZORPAY_KEY_ID,
                "amount": razorpay_order['amount'],
                "product_name": product.title,
                "razorpay_callback_url": settings.RAZORPAY_CALLBACK_URL,
            })

        except Exception as e:
            logger.error("Payment creation failed: %s", str(e))
            return JsonResponse({'error': 'Internal Server Error'}, status=500)