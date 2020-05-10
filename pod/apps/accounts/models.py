import uuid
from django.db import models
from pod.apps.groups.models import Group


class Account(models.Model):
    class Meta:
        db_table = 'Cuentas'

    id = models.CharField(primary_key=True, default=str(uuid.uuid4())[-6:-1].upper(), editable=False, max_length=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='grupo_id')
    status = models.CharField(max_length=50, db_column='status')
    amount = models.CharField(max_length=50, db_column='monto')
    balance = models.CharField(max_length=50, db_column='saldo')

    @classmethod
    def create(cls, *args):
        id, group, status, amount, balance = args
        Account.objects.create(id=id, group_id=group, status=status, amount=amount, balance=balance)