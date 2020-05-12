import uuid
import datetime
from django.db import models
from pod.apps.accounts.models import Account


class Transaction(models.Model):
    class Meta:
        db_table = 'Transacciones'

    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='cuenta_id')
    date = models.DateTimeField(db_column='fecha', auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, db_column='monto')

    @classmethod
    def create(cls, *args):
        id, account, date, amount = args
        Transaction.objects.create(id=id, account_id=account, date=datetime.datetime.strptime(date, "%d/%m/%y %H:%M"),
                                   amount=amount)