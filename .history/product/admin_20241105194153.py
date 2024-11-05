from django.contrib import admin

from .models import Product,ProductImage,Transaction,Order Customer
State
Category
Product
ProductImage
Features
Plan
PaymentType(models.Model):
    name=models.CharField(max_length=100)
class Transaction
list_models=[
    Product,

    ProductImage
]
for model in list_models:
    admin.site.register(model)
