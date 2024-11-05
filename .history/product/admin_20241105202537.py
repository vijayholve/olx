from django.contrib import admin

from .models import Product,ProductImage,Transaction,Order ,Customer, State,Category,Product,ProductImage,Features,Plan,PaymentType
list_models=[
Transaction,Order ,Customer, State,Category,Product,ProductImage,Features,Plan,PaymentType
]
for model in list_models:
    admin.site.register(model)
