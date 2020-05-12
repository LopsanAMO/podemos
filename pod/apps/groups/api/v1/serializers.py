from rest_framework import serializers
from pod.apps.groups.models import Group, Members
from pod.apps.accounts.models import Account
from pod.apps.users.models import Client
from pod.apps.accounts.api.v1.serializers import AccountDetailSerializer


class GroupListSerializer(serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField()
    miembros = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('nombre', 'miembros', 'id')

    def get_nombre(self, obj):
        return obj.name

    def get_miembros(self, obj):
        return Members.objects.filter(group_id=obj.id).values_list('client__name')


class GroupAccountSerializert(serializers.ModelSerializer):
    cuentas = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('cuentas', )

    def get_cuentas(self, obj):
        accounts = Account.objects.filter(group_id=obj.id)
        return AccountDetailSerializer(accounts, many=True).data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'id')
        read_only_fields = ('id',)


class GroupMemberSerializer(serializers.Serializer):
    members = serializers.ListField(required=True)

    def validate(self, attrs):
        try:
            self.clients = Client.objects.filter(id__in=attrs.get('members'))
        except Exception as e:
            raise serializers.ValidationError('Members not found', code=404)
        return attrs


