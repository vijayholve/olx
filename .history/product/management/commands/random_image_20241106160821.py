import os
import random
from django.core.files import File
from product.models import Product, ProductImage
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating fake data...")
        image_directory = rf"media\product_images"

# Get a list of all images in the directory
        image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

        # For each product, add four random images
        for product in Product.objects.all():
            if product.images.count() < 4:  # Ensure there are fewer than 4 images to avoid duplicates
                for _ in range(4 - product.images.count()):
                    # Select a random image file
                    image_file = random.choice(image_files)
                    image_path = os.path.join(image_directory, image_file)

                    # Create a new ProductImage instance
                    with open(image_path, 'rb') as img:
                        product_image = ProductImage(product=product)
                        product_image.image.save(image_file, File(img), save=True)
                        self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))
        self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))

