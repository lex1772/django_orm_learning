from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def send_email():
    send_mail(
        "Поздравляем!",
        "100 просмотров на посте",
        EMAIL_HOST_USER,
        recipient_list=[]
    )