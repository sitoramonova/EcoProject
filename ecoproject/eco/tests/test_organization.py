from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Organization


def test_example():
    assert 1 == 1


class OrganizationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.org = Organization.objects.create(name="Test Organization")

    def test_create_organization(self):
        url = reverse('organization-list')
        data = {"name": "New Organization"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_organization(self):
        url = reverse('organization-detail', args=[self.org.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.org.name)