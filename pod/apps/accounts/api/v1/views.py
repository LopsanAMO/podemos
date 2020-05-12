from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from pod.apps.accounts.api.v1.serializers import CreateAccountSerializer
from pod.apps.accounts.models import Account


class AccountViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer
    permission_classes = (AllowAny, )
