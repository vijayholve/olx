from django.contrib import admin

from .models import Product,ProductImage

list_models=[
    pro
]
admin.site.register(Product)
