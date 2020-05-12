from rest_framework import serializers
from pod.apps.transactions.models import Transaction


class TransactionSeralizer(serializers.ModelSerializer):
    fecha = serializers.SerializerMethodField()
    monto = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ('fecha', 'monto')

    def get_fecha(self, obj):
        return obj.date

    def get_monto(self, obj):
        return obj.amount


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('date', 'amount', 'account')
        extra_kwargs = {
            'date': {'write_only': True},
            'amount': {'write_only': True},
            'account': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs.get('amount') > attrs['account'].balance:
            raise serializers.ValidationError('The amount to deposit cannot be greater than the balance')
        return attrs

    def create(self, validated_data):
        transaction = Transaction.objects.create(**validated_data)
        account = transaction.account
        account.balance -= transaction.amount
        if account.balance == 0.0:
            account.status = 'fin'
        account.save()
        return transaction
