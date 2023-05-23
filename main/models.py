from django.db import models

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
    creation_date = models.DateTimeField(verbose_name='дата создания')
    last_modified = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.description} {self.category} {self.price} {self.creation_date} {self.last_modified}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    contact_email = models.CharField(max_length=100, verbose_name='электронная почта')

    def __str__(self):
        return f'{self.name} {self.contact_email}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
