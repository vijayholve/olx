import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from product.models import Product, ProductImage  # Adjust the import according to your app structure

class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating fake data...")
        
        image_directory = os.path.join("media", "product_images")  # Path to your media folder
        
        # Get a list of all images in the directory
        try:
            image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Directory {image_directory} not found!"))
            return

        if not image_files:
            self.stdout.write(self.style.ERROR("No images found in the directory!"))
            return

        # For each product, add random images
        for product in Product.objects.all():
            # Ensure there are fewer than 4 images to avoid duplicates
            existing_images = product.productimage_set.count()  # Assuming related_name is 'productimage_set'

            # Add images if there are less than 4
            while existing_images < 4:
                # Select a random image file from the directory
                image_file = random.choice(image_files)
                print(f"Selected image: {image_file}")
                image_path = os.path.join(image_directory, image_file)

                try:
                    # Open the image file as a 'File' object
                    with open(image_path, 'rb') as img:
                        # Create and save the ProductImage instance
                        product_image = ProductImage(product=product)
                        product_image.image.save(image_file, File(img), save=True)

                        # Increment the image count for the product
                        existing_images += 1
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error saving image {image_file}: {e}"))

        self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))
