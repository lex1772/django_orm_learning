import json
from datetime import datetime

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.db.transaction import commit
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

from main.models import Product, Contacts, Category
from .forms import ProductForms


# Create your views here.
def home(request):
    products = Product.objects.all()[len(Product.objects.all()) - 5:len(Product.objects.all())]
    if request.POST:
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            product_name = cd.get('product_name')
            description = cd.get('description')
            image = cd.get('image')
            category = cd.get('category').lower()
            price = cd.get('price')
            cat = Category.objects.get(category=category)
            creation_date = datetime.now()
            last_modified = datetime.now()
            product = Product(product_name=product_name, description=description, image=image, category=cat,
                              price=price, creation_date=creation_date, last_modified=last_modified)
            product.save()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(products, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    for i in products:
        print(i)
    return render(request, 'main/home.html', {'products': products, 'page_obj': page_obj, 'form': ProductForms})


def contact(request):
    contacts = Contacts.objects.all()
    print(contacts)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/contact.html', {'contacts': contacts})
