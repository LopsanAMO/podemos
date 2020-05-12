from nose.tools import eq_, ok_
from django.test import TestCase
from django.forms.models import model_to_dict
from pod.apps.users.test.factories import ClientFactor
from pod.apps.groups.test.factories import GroupFactory
from pod.apps.groups.api.v1.serializers import GroupSerializer, GroupMemberSerializer


class TestGroupSerializer(TestCase):
    def setUp(self):
        self.group_data = model_to_dict(GroupFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = GroupSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = GroupSerializer(data=self.group_data)
        ok_(serializer.is_valid())


class TestGroupMemberSerializer(TestCase):
    def setUp(self):
        self.clients = {"members": []}
        for i in range(1, 10):
            model = ClientFactor()
            self.clients['members'].append(model.id)

    def test_serializer_with_empty_data(self):
        serializer = GroupMemberSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = GroupMemberSerializer(data=self.clients)
        ok_(serializer.is_valid())
