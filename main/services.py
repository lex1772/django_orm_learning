from django.core.cache import cache
from django.core.mail import send_mail

from config import settings
from config.settings import EMAIL_HOST_USER
from main.models import Product


def send_email():
    send_mail(
        "Поздравляем!",
        "100 просмотров на посте",
        EMAIL_HOST_USER,
        recipient_list=[]
    )

def get_cached_for_product_list():
    if settings.CACHE_ENABLED:
        key = f'product_list'
        object_list = cache.get(key)
        if object_list is None:
            object_list = Product.objects.all()
            cache.set(key, object_list)
    else:
        object_list = Product.objects.all()

    return object_list