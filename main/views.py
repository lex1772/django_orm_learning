import json
from datetime import datetime

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.db.transaction import commit
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from django.views import generic

from main.models import Product, Contacts, Category, Blog, Version
from .forms import ProductForm, VersionForm
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
    form_class = ProductForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ParentFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ParentFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ("name", "post", "image")
    success_url = reverse_lazy('main:blog')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    fields = ("name", "post", "image", "slug")
    success_url = reverse_lazy('main:blog')
