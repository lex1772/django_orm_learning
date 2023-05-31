import json
from datetime import datetime

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.db.transaction import commit
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from django.views import generic

from main.models import Product, Contacts, Category, Blog
from .forms import ProductForms
from .services import send_email


# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    paginate_by = 1
    extra_context = {
        'title': 'Продукты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/product.html'


class ProductCreateView(generic.CreateView):
    model = Product
    fields = ("product_name", "description", "category", "price")
    success_url = reverse_lazy('main:home')


class ProductUpdateView(generic.UpdateView):
    model = Product
    fields = ("product_name", "description", "category", "price")
    success_url = reverse_lazy('main:home')


class ProductDeleteView(generic.DeleteView):
    model = Product
    fields = ("product_name", "description", "category", "price")
    success_url = reverse_lazy('main:home')


class ContactsCreateView(generic.CreateView):
    model = Contacts
    fields = ("name", "contact_email", "message")
    success_url = reverse_lazy('main:home')


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 3
    extra_context = {
        'title': 'Блог'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(likes=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self):
        obj = super().get_object()
        obj.total_views += 1
        obj.save()
        if obj.total_views == 100:
            send_email()
        return obj


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ("name", "post", "image")
    #def new_post_redirect(request, slug):
        #post_item = get_object_or_404(Blog, slug=slug)
        #return redirect(reverse("main:post_item", args=[post_item.pk]))


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ("name", "post", "image")
    success_url = reverse_lazy('main:blog')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    fields = ("name", "post", "image", "slug")
    success_url = reverse_lazy('main:blog')
