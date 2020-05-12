import random
from rest_framework import serializers
from pod.apps.accounts.models import Account
from pod.apps.transactions.api.v1.serializers import TransactionSeralizer
from pod.apps.payments.api.v1.serializers import PaymentCalendarSerializer
from pod.apps.payments.models import PaymentCalendar
from pod.apps.transactions.models import Transaction


class AccountDetailSerializer(serializers.ModelSerializer):
    calendario = serializers.SerializerMethodField()
    transacciones = serializers.SerializerMethodField()
    estatus = serializers.SerializerMethodField()
    monto = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('monto', 'balance', 'calendario', 'transacciones', 'id', 'estatus')

    def get_estatus(self, obj):
        return Account.STATUS.get_value(obj.status)

    def get_monto(self, obj):
        return obj.amount

    def get_calendario(self, obj):
        pay_calendar = PaymentCalendar.objects.filter(account_id=obj.id)
        return PaymentCalendarSerializer(pay_calendar, many=True).data

    def get_transacciones(self, obj):
        transactions = Transaction.objects.filter(account_id=obj.id)
        return TransactionSeralizer(transactions, many=True).data

    def to_representation(self, instance):
        ret = super(AccountDetailSerializer, self).to_representation(instance)
        for key, value in ret.items():
            if value is None:
                ret[key] = ''
        return ret


class CreateAccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        to_choice = "0123456789ABCDEFGHI"
        client = Account.objects.create(
            group=validated_data['group'],
            amount=validated_data['amount'],
            balance=validated_data['balance'],
            num_payments=validated_data['num_payments'],
            id=''.join(random.choice(to_choice) for i in range(7))
        )
        return client

    class Meta:
        model = Account
        fields = ('group', 'amount', 'balance', 'num_payments')


