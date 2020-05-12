import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username


class Client(models.Model):
    class Meta:
        db_table = 'Clientes'

    id = models.CharField(max_length=7, primary_key=True, editable=False)
    name = models.CharField(max_length=50, db_column='nombre', null=False, blank=False)

    @classmethod
    def create(cls, *args):
        id, name = args
        Client.objects.create(name=name, id=id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

