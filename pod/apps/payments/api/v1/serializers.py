from rest_framework import serializers
from pod.apps.payments.models import PaymentCalendar


class PaymentCalendarSerializer(serializers.ModelSerializer):
    num_pago = serializers.SerializerMethodField()
    monto = serializers.SerializerMethodField()
    fecha_pago = serializers.SerializerMethodField()
    estatus = serializers.SerializerMethodField()

    class Meta:
        model = PaymentCalendar
        fields = ('num_pago', 'monto', 'fecha_pago', 'estatus')

    def get_num_pago(self, obj):
        return obj.num_payment

    def get_monto(self, obj):
        return obj.amount

    def get_fecha_pago(self, obj):
        return obj.payment_date

    def get_estatus(self, obj):
        return obj.status

