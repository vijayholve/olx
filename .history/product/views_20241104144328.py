from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State  ,Category
from django import template 
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from itertools import zip_longest

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, ProductImage  # Import your models

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
    context={}
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(category__name__icontains=query)
        )
        
        
    elif category:
        products = Product.objects.filter(category__name=category)
        context['category'] = category
    elif condition:
        products = Product.objects.filter(condition=condition)
        context['query'] = condition
    else:
        products = Product.objects.all()

    productimage = {}
    for product in products:
        image = ProductImage.objects.filter(product=product).first()
        if image:
            productimage[product.id] = image.image  # Store each product's image in the dictionary
    
    # Get all categories for the dropdown or filter options
    all_category = Category.objects.all()

    # Prepare context for rendering the template
    context += {
        'products': products,
        'productimage': productimage,
        'all_category': all_category,
        'query': query,  # Pass the query back to the template to retain the search input
    }

        

    return render(request, "product/home.html", context)


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


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    suggested_products = Product.objects.all().exclude(id=product.id)[:9]  # Fetch up to 9 suggested products

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

    }
    
    return render(request, 'product/product_details.html', context)


