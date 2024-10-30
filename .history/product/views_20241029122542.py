from django.shortcuts import render
from .forms import ProductForm,MultipleImagesForm,ProductImage
from .models import Product ,ProductImage

def create_form(request):
    if request.method == 'POST':
        prod_form=ProductForm(request.POST)
        img_form=MultipleImagesForm(request.POST, request.FILES)
        if prod_form.is_valid() and img_form.is_valid():
            product=prod_form.save(commit=False)
            product.posted_by=request.user 
            product.save()
            images=request.FILES.getlist('images')
            for img in images:
                images_creating=image