import uuid
from django.db import models
from pod.apps.users.models import User


class Group(models.Model):
    class Meta:
        db_table = 'Grupos'

    id = models.CharField(primary_key=True, default=str(uuid.uuid4())[-6:-1].upper(), editable=False, max_length=5)
    member = models.ManyToManyField(User, through='Members', through_fields=('group', 'client'))
    name = models.CharField(max_length=20, db_column='nombre')

    @classmethod
    def create(cls, *args):
        id, name = args
        Group.objects.create(id=id, name=name)


class Members(models.Model):
    class Meta:
        db_table = 'Miembros'

    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='grupo_id')
    client = models.ForeignKey(User, on_delete=models.CASCADE, db_column='cliente_id')

    @classmethod
    def create(cls, *args):
        group, client = args
        Members.objects.create(group_id=group, client_id=client)
