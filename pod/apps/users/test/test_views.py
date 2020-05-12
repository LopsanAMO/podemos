from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory
from ..models import Client
from pod.apps.users.test.factories import ClientFactor

fake = Faker()


class TestCreateClientTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('client-list')
        self.client_data = factory.build(dict, FACTORY_CLASS=ClientFactor)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.client_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        client = Client.objects.get(pk=response.data.get('id'))
        eq_(client.name, self.client_data.get('name'))


class TestUpdateClientTestCase(APITestCase):
    def setUp(self):
        self.cliente = ClientFactor()

    def test_put_request_updates_a_client(self):
        new_name = fake.first_name()
        payload = {'name': new_name}
        response = self.client.put('/api/v1/users/client/%s/'% self.cliente.id, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        client = Client.objects.get(pk=self.cliente.id)
        eq_(client.name, new_name)
