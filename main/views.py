import json
from datetime import datetime

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render

from main.models import Product, Contacts, Category
from .forms import ProductForms


# Create your views here.
def home(request):
    products = Product.objects.all()[len(Product.objects.all()) - 5:len(Product.objects.all())]
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


def index(request):
    object_list = Product.objects.all()[len(Product.objects.all()) - 5:len(Product.objects.all())]
    page_num = request.GET.get('page', 1)

    paginator = Paginator(object_list, 1)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'main/home.html', {'page_obj': page_obj})


def add_product(request):
    product_form = ProductForms(request.POST, request.FILES)
    if product_form.is_valid():
        form = product_form.save(commit=False)
        form.save()
    else:
        product_form = ProductForms()

    return render(request, 'main/home.html', {'product_form': product_form})
