from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    location = models.CharField(max_length=255)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To allow listing activation/deactivation
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title