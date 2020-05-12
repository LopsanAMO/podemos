from rest_framework.permissions import AllowAny
from rest_framework import mixins, viewsets
from pod.apps.transactions.models import Transaction
from pod.apps.transactions.api.v1.serializers import CreateTransactionSerializer


class TransactionCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = CreateTransactionSerializer
    permission_classes = (AllowAny, )