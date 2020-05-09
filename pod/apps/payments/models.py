import uuid
from django.db import models
from pod.apps.accounts.models import Account


class PaymentCalendar(models.Model):
    class Meta:
        db_table = 'CalendarioPagos'

    id = models.IntegerField(primary_key=True, default=int(str(uuid.uuid4().fields[-1])[:11]), editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, db_column='cuenta_id')
    num_payment = models.CharField(max_length=50, db_column='num_pago')
    amount = models.CharField(max_length=50, db_column='monto')
    payment_date = models.DateTimeField(db_column='fecha_pago')
    status = models.CharField(max_length=50, db_column='estatus')
