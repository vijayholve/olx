from django.shortcuts import render

# Create your views here.


def create_form(request):
    if request.method == 'POST':
        # get form data
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']