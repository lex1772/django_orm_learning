import json

from django.core.management import BaseCommand

from main.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('data.json', encoding='utf-8') as file:
            data = json.load(file)
            category_list = []
            product_list = []
            for i in data:
                if i['model'] == 'main.category':
                    category_list.append(Category(**i['fields']))
            Category.objects.bulk_create(category_list)
            for j in data:
                if j['model'] == 'main.product':
                    category_to_search = "".join(j['fields']['description']).split()
                    for i in Category.objects.only():
                        if i.category.startswith(category_to_search[0]):
                            j['fields']['category'] = i
                    product_list.append(Product(**j['fields']))
            Product.objects.bulk_create(product_list)
