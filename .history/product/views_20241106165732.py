from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State  ,Category
from django import template 
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from itertools import zip_longest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    # if  query and category and condition:
    #     products = Product.objects.filter(
    #         Q(title__icontains=query) | 
    #         Q(category__name__icontains=query)
    #     ).filter(category__name=category, condition=condition)
    # elif query and condition:
    #     products = Product.objects.filter(
    #         Q(title__icontains=query) | 
    #         Q(category__name__icontains=query)
    #     ).filter(condition=condition)

    # elif query and category:
    #     products = Product.objects.filter(
    #         Q(title__icontains=query) | 
    #         Q(category__name__icontains=query)
    #     ).filter(category__name=category)
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
        products = Product.objects.all()

    productimage = {}
    for product in products:
        if image := ProductImage.objects.filter(product=product).first():
            productimage[product.id] = image.image  # Store each product's image in the dictionary

    # Get all categories for the dropdown or filter options
    all_category = Category.objects.all()

    # Prepare context for rendering the template
    context = {
        'products': products,
        'productimage': productimage,
        'all_category': all_category,
        'query': query,  # Pass the query back to the template to retain the search input
    }
    context.update(context1)
    return render(request, "product/home.html", context)

@login_required(login_url='login-page')
def product_create_form(request):
    number_of_image_fields = 4
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = MultipleImagesForm(request.FILES)
        print(product_form)
        print(image_form)

        if product_form.is_valid() or image_form.is_valid():
            product = product_form.save(commit=False)
            product.posted_by = request.user
            product.save()

            # Handle the images
            images = request.FILES.getlist('images')
            
            for img in images:
                ProductImage.objects.create(product=product, image=img)

            return redirect('home')
    else:
        product_form = ProductForm()
        image_form = MultipleImagesForm()

    context = {
        'number_of_image_fields': range(number_of_image_fields),  # Pass the range as context
        'product_form': product_form,
        'image_form': image_form,
    }

    return render(request, 'product/create_product.html', context)

@login_required(login_url='login-page')
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    suggested_products = Product.objects.all().exclude(id=product.id)[:9]  # Fetch up to 9 suggested products
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
                for pro in ProductImage.objects.filter(product=product) :
                    # product.productimage_set.all().delete()
                    p

                # Add new images
                images = request.FILES.getlist('images')
                for img in images:
                    ProductImage.objects.create(product=product, image=img)

            return redirect('home')  # Redirect to the home page or product list

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
