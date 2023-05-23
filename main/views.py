import json

from django.core import serializers
from django.shortcuts import render

from main.models import Product, Contacts


# Create your views here.
def home(request):
    products = Product.objects.all()[len(Product.objects.all())-5:len(Product.objects.all())]
    for i in products:
        print(i)
    return render(request, 'main/home.html', {'products': products})


def contact(request):
    contacts = Contacts.objects.all()
    print(contacts)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/contact.html', {'contacts': contacts})

