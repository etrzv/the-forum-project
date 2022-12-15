'''import time
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


UserModel = get_user_model()
# TODO: celery async task added:

@shared_task
def send_welcome_email_to_new_users(email):  # if we had parameters here we put them in the delay
    user = UserModel.objects.get(email=email)
    user.send_activation_email()'''


