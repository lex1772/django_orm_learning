# Generated by Django 4.2.1 on 2023-05-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('post', models.CharField(max_length=100, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('likes', models.BooleanField(default=True, verbose_name='признак публикации')),
                ('total_views', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
        ),
    ]
