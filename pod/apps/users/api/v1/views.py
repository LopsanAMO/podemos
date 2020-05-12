from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from pod.apps.users.api.v1.serializers import ClientListSerializer, CreateClientSerializer
from pod.apps.users.models import User, Client
from pod.apps.users.api.v1.serializers import CreateUserSerializer


class ClientListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer
    permission_classes = (AllowAny, )


class CreateClientViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer
    permission_classes = (AllowAny, )


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)
