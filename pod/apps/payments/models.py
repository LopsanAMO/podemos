import uuid
import datetime
from enum import Enum
from django.db import models
from pod.apps.accounts.models import Account


class PaymentCalendar(models.Model):
    class STATUS(Enum):
        pen = ('pen', 'PENDIENTE')
        pag = ('pag', 'PAGADO')
        par = ('par', 'PARCIAL')
        atr = ('atr', 'ATRASADO')

        @classmethod
        def get_value(cls, val):
            try:
                return cls[val].value[1]
            except KeyError:
                return False

    class Meta:
        db_table = 'CalendarioPagos'

    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='cuenta_id')
    num_payment = models.IntegerField(db_column='num_pago')
    amount = models.DecimalField(max_digits=15, decimal_places=2, db_column='monto')
    payment_date = models.DateField(db_column='fecha_pago')
    status = models.CharField(max_length=15, db_column='estatus', choices=[x.value for x in STATUS], default='pen')

    @classmethod
    def create(cls, *args):
        id, account, num_payment, amount, payment_date, status = args
        PaymentCalendar.objects.create(id=id, account_id=account, num_payment=num_payment, amount=amount,
                                       payment_date=datetime.datetime.strptime(payment_date, "%Y-%m-%d"),
                                       status=status)

    def __str__(self):
        return "pago de {}".format(self.account)
