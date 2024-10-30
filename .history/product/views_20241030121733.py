from django.shortcuts import render,redirect
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage,State  ,Category
from django import template 
from django.db.models import Q
register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)


from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, ProductImage  # Import your models

def home(request):
    category = request.GET.get('category', '')
    query = request.GET.get('search', '')  # Ensure this matches the name attribute in your search input

    # Filter products based on search query and category
    if query and category:
        # Both search query and category are provided
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(category__name__icontains=query)
        ).filter(category__name=category)
    elif query:
        # Only search query is provided
        products = Product.objects.filter(
            Q(title__icontains=query) | 
            Q(category__name__icontains=query)
        )
    elif category:
        # Only category is provided
        products = Product.objects.filter(category__name=category)
    else:
        # No filters applied, fetch all products
        products = Product.objects.all()

    # Retrieve the first image for each product
    productimage = {}
    for product in products:
        image = ProductImage.objects.filter(product=product).first()
        if image:
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




def product_details(request,product_id):
    product = Product.objects.get(id=product_id)
    image = ProductImage.objects.filter(product=product).first()
    context = {
        'product': product,
        'image': image,
    }
    return render(request, 'product/product_details.html', context)