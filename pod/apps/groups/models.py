import uuid
import random
from django.db import models
from pod.apps.users.models import Client


class Group(models.Model):
    class Meta:
        db_table = 'Grupos'

    id = models.CharField(primary_key=True, editable=False, max_length=5)
    member = models.ManyToManyField(Client, through='Members', through_fields=('group', 'client'))
    name = models.CharField(max_length=20, db_column='nombre', unique=True, blank=False)

    @classmethod
    def create(cls, *args):
        id, name = args
        Group.objects.create(id=id, name=name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = ''.join(random.choice("0123456789ABCDEFGHI") for i in range(5))
        super(Group, self).save(*args, **kwargs)


class Members(models.Model):
    class Meta:
        db_table = 'Miembros'

    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='grupo_id')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='cliente_id')

    @classmethod
    def create(cls, *args):
        group, client = args
        Members.objects.create(group_id=group, client_id=client)
