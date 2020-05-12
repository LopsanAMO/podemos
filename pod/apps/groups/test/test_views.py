import factory
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from pod.apps.users.test.factories import ClientFactor
from pod.apps.accounts.test.factories import AccountFactory
from pod.apps.groups.test.factories import GroupFactory
from pod.apps.groups.models import Group


class TestgGroupListTestCase(APITestCase):
    def test_get_request_returns_a_group_list(self):
        response = self.client.get("/api/v1/groups/members/")
        eq_(response.status_code, status.HTTP_200_OK)


class TestGroupDetailTestCase(APITestCase):
    def setUp(self) :
        self.account_data = AccountFactory.create()

    def test_get_request_returns_a_group_list(self):
        response = self.client.get("/api/v1/groups/detail/%s/"% self.account_data.group.id)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_get_request_returns_a_group_list_failed(self):
        response = self.client.get("/api/v1/groups/detail/B342/")
        eq_(response.status_code, status.HTTP_404_NOT_FOUND)


class TestGroupTestCase(APITestCase):
    def setUp(self):
        self.group_data = factory.build(dict, FACTORY_CLASS=GroupFactory)
        self.url = "/api/v1/groups/group/"

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.group_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        group = Group.objects.get(pk=response.data.get('id'))
        eq_(group.name, self.group_data.get('name'))

    def test_update_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_request_with_valid_data_succeeds(self):
        new_name = 'GrupoTest'
        group = GroupFactory.create()
        response = self.client.put("/api/v1/groups/group/%s/"% group.id, {'name': new_name})
        eq_(response.status_code, status.HTTP_200_OK)


class TestGroupMemberTestCase(APITestCase):
    def setUp(self):
        self.group_data = GroupFactory.create()
        self.url = "/api/v1/groups/groups/%s"% self.group_data.id
        self.clients = {"members": []}
        self.to_delete = None
        for i in range(1, 10):
            self.to_delete = ClientFactor.create()
            self.clients['members'].append(self.to_delete.id)

    def test_put_request_with_no_data_fails(self):
        response = self.client.put(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_request_with_valid_data_succeeds(self):
        response = self.client.put(self.url, self.clients)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_delete_request_with_no_data_fails(self):
        response = self.client.delete(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_request_with_valid_data_succeeds(self):
        response = self.client.put(self.url, {'members': [self.to_delete.id]})
        eq_(response.status_code, status.HTTP_200_OK)
