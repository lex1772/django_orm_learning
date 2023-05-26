import json
from datetime import datetime

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.shortcuts import render

from main.models import Product, Contacts
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


def post_list(request):
    object_list = Product.objects.all()[len(Product.objects.all()) - 5:len(Product.objects.all())]
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'main/home.html',
                  {'page': page,
                   'posts': posts})


def product(request):
    submitbutton = request.POST.get("submit")

    product_name = ''
    price = ''
    category = ''
    description = ''

    form = ProductForms(request.POST or None)
    if form.is_valid():
        product_name = form.cleaned_data.get("product_name")
        price = form.cleaned_data.get("price")
        category = form.cleaned_data.get("category")
        description = form.cleaned_data.get("description")
        creation_date = datetime.now()
        last_modified = datetime.now()

    context = {'form': form, 'product_name': product_name,
               'price': price, 'category': category,
               'description': description}

    new_product = Product.objects.create(product_name=product_name, price=price, category=category,
                                         description=description, creation_date=creation_date,
                                         last_modified=last_modified)

    return render(request, 'main/home.html', context)
