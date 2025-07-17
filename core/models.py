from django.contrib.auth.models import AbstractUser
from django.db import models

from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage


class User(AbstractUser):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='username')
    surname = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    search_plan = models.CharField(max_length=50, choices=[('free', 'Free'), (
        'standard', 'Standard'), ('business', 'Business'), ('premium', 'Premium')], default='free')
    search_count = models.IntegerField(default=0)
    progress_count = models.IntegerField(default=0)
    searches_allowed = models.IntegerField(default=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def max_searches(self):
        return {
            'free': 8,
            'standard': 35,
            'business': 50,
            'premium': 100
        }.get(self.search_plan)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "Hola" + "\n" + "Gracias por comunicarte con Lexcom" + "\n" + "Abra el enlace para restablecer su contraseña" + \
        " " + "{}{}".format(instance.request.build_absolute_uri(
            "https://lexcom.tech/reset-password-form/"), reset_password_token.key)

    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        "Password Reset for {title}".format(
            title="Crediation Lexcom portal account"),
        email_plaintext_message,
        "suptechlexcom1@gmail.com",
        [reset_password_token.user.email],
        fail_silently=False,
    )
