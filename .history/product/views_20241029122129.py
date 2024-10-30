from django.shortcuts import render
from 
# Create your views here.


def create_form(request):
    if request.method == 'POST':
        prod_form=