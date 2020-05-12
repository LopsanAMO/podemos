import factory
from pod.apps.users.test.factories import UserFactory


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'groups.Group'

    id = factory.Sequence(lambda n: f'B{n}')
    name = factory.Sequence(lambda n: f'group{n}')


class MemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'groups.Members'

    group = factory.SubFactory(GroupFactory)
    client = factory.SubFactory(UserFactory)

