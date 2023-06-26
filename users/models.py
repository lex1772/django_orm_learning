from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    email_verify = models.BooleanField(default=False)

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class StatusType(models.Model):
        MODERATOR = "MODERATOR"
        BASE_USER = "BASE_USER"
        CONTENT_MANAGER = "CONTENT_MANAGER"
        STATUS = [
            (MODERATOR, "Moderator"),
            (BASE_USER, "Base_user"),
            (CONTENT_MANAGER, "Content_manager"),
        ]

    status_type = models.CharField(
        max_length=50,
        choices=StatusType.STATUS,
        default=StatusType.BASE_USER,
        verbose_name="роль")
