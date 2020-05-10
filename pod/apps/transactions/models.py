import uuid
import datetime
from django.db import models
from pod.apps.accounts.models import Account


class Transaction(models.Model):
    class Meta:
        db_table = 'Transacciones'

    id = models.IntegerField(primary_key=True, default=int(str(uuid.uuid4().fields[-1])[:11]), editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='cuenta_id')
    date = models.DateTimeField(db_column='fecha')
    amount = models.CharField(max_length=50, db_column='monto')

    @classmethod
    def create(cls, *args):
        id, account, date, amount = args
        Transaction.objects.create(id=id, account_id=account, date=datetime.datetime.strptime(date, "%d/%m/%y %H:%M"),
                                   amount=amount)