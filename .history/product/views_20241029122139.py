from django.shortcuts import render
from .forms import ProductForm,MultipleImagesForm
# Create your views here.


def create_form(request):
    if request.method == 'POST':
        prod_form=