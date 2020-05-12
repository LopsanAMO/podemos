from nose.tools import eq_, ok_
from django.test import TestCase
from django.forms.models import model_to_dict
from pod.apps.accounts.test.factories import AccountFactory
from pod.apps.groups.test.factories import GroupFactory
from pod.apps.accounts.api.v1.serializers import CreateAccountSerializer


class TestCreateAccountSerializer(TestCase):
    def setUp(self):
        self.account_data = model_to_dict(AccountFactory.build())
        self.group_data = GroupFactory.create()

    def test_serializer_with_empty_data(self):
        serializer = CreateAccountSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        self.account_data['group'] = self.group_data.id
        serializer = CreateAccountSerializer(data=self.account_data)
        ok_(serializer.is_valid())