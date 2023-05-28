from datetime import datetime

from django.forms import forms, CharField, ImageField, IntegerField, DateTimeField, ModelForm

from main.models import Category, Product


class ProductForms(forms.Form):
    product_name = CharField(max_length=100)
    description = CharField(max_length=100)
    image = ImageField(required=False)
    category = CharField(max_length=100)
    price = IntegerField()
    creation_date = datetime.now()
    last_modified = datetime.now()
    class Meta:
        model = Product
        fields = ["product_name", "description", "category", "price"]
        category = Category
