from django.contrib import admin

from main.models import Category, Product, Contacts, Blog, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    list_filter = ('category',)
    search_fields = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category', )
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', )
    list_filter = ('name', 'contact_email', )
    search_fields = ('name', 'contact_email', )

@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "slug", )

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'title', 'is_active', )
    list_filter = ('number', 'title', )
    search_fields = ('number', 'title', )