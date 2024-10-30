from django.shortcuts import render

# Create your views here.


def create_form(request):
    if request.method == 'POST':
        prod_form=