from django.db import models
from django.urls import reverse
from transliterate import slugify

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.category} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    is_active = models.BooleanField(default=True, verbose_name='активный')

    def __str__(self):
        return f'{self.product_name} {self.description} {self.category} {self.price} {self.creation_date} {self.last_modified}'

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    contact_email = models.EmailField(max_length=100, verbose_name='электронная почта')
    message = models.CharField(default="", max_length=100, verbose_name='сообщение')

    def __str__(self):
        return f'{self.name} {self.contact_email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    post = models.CharField(max_length=100, verbose_name='содержимое')
    image = models.ImageField(upload_to='img/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    likes = models.BooleanField(default=True, verbose_name='признак публикации')
    total_views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.name} {self.slug} {self.post} {self.creation_date} {self.creation_date} {self.total_views}'

    def dont_show(self, *args, **kwargs):
        self.likes = False
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:blog', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'блог'
