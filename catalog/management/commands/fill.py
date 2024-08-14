import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("catalog_data.json", encoding="utf-8") as file:
            values = json.load(file)
        categories = [value for value in values if value['model'] == "catalog.category"]
        return categories

    @staticmethod
    def json_read_products():
        with open("catalog_data.json", encoding='utf-8') as file:
            values = json.load(file)
        products = [value for value in values if value['model'] == 'catalog.product']
        return products

    def handle(self, *args, **options):
        # Удаление всех продуктов
        Product.objects.all().delete()
        # Удаление всех продуктов
        Category.objects.all().delete()

        # списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Перебор значений категорий из фикстуры
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category.get('pk'),
                         category_name=category.get('fields').get('category_name'),
                         category_description=category.get('fields').get('category_description'))
            )

        # создание категорий
        Category.objects.bulk_create(category_for_create)

        # Перебор значений товаров из фикстуры
        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product.get("pk"),
                        product_name=product.get('fields').get('product_name'),
                        product_description=product.get('fields').get('product_description'),
                        product_picture=product.get('fields').get('product_picture'),
                        category=Category.objects.get(pk=product.get('fields').get('category')),
                        price=product.get('fields').get('price'),
                        created_at=product.get('fields').get('created_at'),
                        updated_at=product.get('fields').get('updated_at'))
            )

        # создание товаров
        Product.objects.bulk_create(product_for_create)
