from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from pod.apps.groups.models import Group, Members
from pod.apps.groups.api.v1.serializers import GroupListSerializer, GroupAccountSerializert, GroupSerializer,\
    GroupMemberSerializer


class GroupMembersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = (AllowAny, )


class GroupAccountListViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupAccountSerializert
    permission_classes = (AllowAny, )
    lookup_value_regex = '[a-zA-Z0-9]+'


class GroupViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class GroupMemeberAPIView(APIView):
    permission_classes = (AllowAny, )

    def put(self, request, *args, **kwargs):
        serializer = GroupMemberSerializer(data=request.data)
        if serializer.is_valid():
            for client in serializer.clients:
                member, create = Members.objects.get_or_create(group_id=kwargs['group_id'], client=client)
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        serializer = GroupMemberSerializer(data=request.data)
        if serializer.is_valid():
            for client in serializer.clients:
                Members.objects.filter(group_id=kwargs['group_id'], client=client).delete()
            return Response(status=200)
        else:
            return Response(serializer.errors, status=400)

