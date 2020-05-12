import factory
from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from pod.apps.accounts.test.factories import AccountFactory
from pod.apps.groups.test.factories import GroupFactory


class TestCreateAccountTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('account-list')
        self.client_data = factory.build(dict, FACTORY_CLASS=AccountFactory)
        self.group_data = GroupFactory.create()
        self.client_data['group'] = self.group_data.id

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.client_data)
        eq_(response.status_code, status.HTTP_201_CREATED)
