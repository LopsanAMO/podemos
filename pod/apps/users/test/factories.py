import factory
from pod.apps.users.models import Client


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'
        django_get_or_create = ('username',)

    id = factory.Faker('uuid4')
    username = factory.Sequence(lambda n: f'testuser{n}')
    password = factory.Faker('password', length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False


class ClientFactor(factory.django.DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.Faker('first_name')
    id = factory.Sequence(lambda n: f'ABCD{n}')
