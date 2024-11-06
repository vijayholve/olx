import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from product.models import Product, ProductImage  # Adjust according to your app structure

class Command(BaseCommand):
    help = "Generate fake data for testing"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating fake data...")
        
        # Ensure the correct path to the media folder
        image_directory = os.path.join("media", "product_images")  # Use os.path.join for portability
        if image_directory:
            print(image_directory)
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
            existing_images = 0
            # Add images if there are less than 4
            while existing_images < 4:
                # Select a random image file from the directory
                
                image_file = random.choice(image_files)
                print(image_file)
                image_path = os.path.join(image_directory, image_file)

                # Create a new ProductImage instance and save it
                with open(image_path, 'rb') as img:
                        # Create and save the ProductImage instance
                        product_image = ProductImage(product=product)
                        product_image.image.save(image_file, File(img), save=True)
                    # Increment the image count for the product
                        existing_images += 1

        self.stdout.write(self.style.SUCCESS("Successfully created fake data!"))
