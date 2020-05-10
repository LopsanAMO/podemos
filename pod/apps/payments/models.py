import uuid
import datetime
from django.db import models
from pod.apps.accounts.models import Account


class PaymentCalendar(models.Model):
    class Meta:
        db_table = 'CalendarioPagos'

    id = models.IntegerField(primary_key=True, default=int(str(uuid.uuid4().fields[-1])[:11]), editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='cuenta_id')
    num_payment = models.CharField(max_length=50, db_column='num_pago')
    amount = models.CharField(max_length=50, db_column='monto')
    payment_date = models.DateField(db_column='fecha_pago')
    status = models.CharField(max_length=50, db_column='estatus')

    @classmethod
    def create(cls, *args):
        id, account, num_payment, amount, payment_date, status = args
        PaymentCalendar.objects.create(id=id, account_id=account, num_payment=num_payment, amount=amount,
                                       payment_date=datetime.datetime.strptime(payment_date, "%Y-%m-%d"),
                                       status=status)
