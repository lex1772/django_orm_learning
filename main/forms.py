from django.forms import forms, CharField, ImageField, IntegerField, DateTimeField, ModelForm

from main.models import Category


class ProductForms(forms.Form):
    product_name = CharField(max_length=100)
    description = CharField(max_length=100)
    image = ImageField()
    category = CharField(max_length=100)
    price = IntegerField()
    creation_date = DateTimeField()
    last_modified = DateTimeField()