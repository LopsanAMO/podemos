import random
from rest_framework import serializers
from pod.apps.users.models import User, Client


class ClientListSerializer(serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ('nombre', 'id')

    def get_nombre(self, obj):
        return obj.name


class CreateClientSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        to_choice = "0123456789ABCDEFGHI"
        client = Client.objects.create(
            name=validate_data['name'],
            id=''.join(random.choice(to_choice) for i in range(7))
        )
        return client

    class Meta:
        model = Client
        fields = ('name', 'id')
        extra_kwargs = {
            'name': {'write_only': True}
        }
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True}
        }
