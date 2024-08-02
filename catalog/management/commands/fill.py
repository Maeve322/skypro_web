from django.core.management.base import BaseCommand

from catalog.models import Category, Product
import json


class Command(BaseCommand):
    help = "Fill the database with data from JSON file"

    def handle(self, *args, **options):
        # Удаляем все категории и продукты
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open("data.json") as file:
            data = json.load(file)

            # Создаем категории
            for item in data:
                if item["model"] == "catalog.category":
                    category_data = item["fields"]
                    Category.objects.create(
                        id=item["pk"],
                        name=category_data["name"],
                        description=category_data["description"],
                        created_at=category_data["created_at"],
                    )
                elif item["model"] == "catalog.product":
                    product_data = item["fields"]
                    Product.objects.create(
                        id=item["pk"],
                        name=product_data["name"],
                        description=product_data["description"],
                        imagePreview=product_data["imagePreview"],
                        category_id=product_data["category"],
                        created_at=product_data["created_at"],
                        updated_at=product_data["updated_at"],
                        price=product_data["price"],
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "Data successfully filled in the database from JSON file"
            )
        )
