import uuid
import datetime
from enum import Enum
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from pod.apps.groups.models import Group


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value[0], cls))


class Account(models.Model):
    class STATUS(ExtendedEnum):
        ini = ("ini", "DESEMBOLSADA")
        fin = ("fin", "CERRADA")

        @classmethod
        def get_value(cls, val):
            try:
                return cls[val].value[1]
            except KeyError:
                return False

    class Meta:
        db_table = 'Cuentas'

    id = models.CharField(primary_key=True, editable=False, max_length=5)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='grupo_id')
    status = models.CharField(max_length=50, db_column='status', choices=[x.value for x in STATUS], default='ini')
    amount = models.DecimalField(max_digits=15, decimal_places=2, db_column='monto')
    balance = models.DecimalField(max_digits=15, decimal_places=2, db_column='saldo')
    num_payments = models.IntegerField(db_column='num_pagos', default=4)

    @classmethod
    def create(cls, *args):
        id, group, status, amount, balance = args
        Account.objects.create(id=id, group_id=group, status=status, amount=amount, balance=balance)

    def __str__(self):
        return 'cuenta de {} por {}'.format(self.group.name, self.amount)


@receiver(post_save, sender=Account)
def create_payment_calendar(sender, intance=None, created=False, **kwargs):
    from pod.apps.payments.models import PaymentCalendar
    if created and settings.SIGNALS:
        date_now = datetime.datetime.now()
        next_dates = [date_now + datetime.timedelta(i) for i in range(7, 7*(kwargs['instance'].num_payments + 1), 7)]
        amount_per_week = kwargs['instance'].amount / kwargs['instance'].num_payments
        for date_index in range(len(next_dates)):
            PaymentCalendar.objects.create(account_id=kwargs['instance'].id, num_payment=date_index+1,
                                           amount=amount_per_week, payment_date=next_dates[date_index],
                                           status='pen')
