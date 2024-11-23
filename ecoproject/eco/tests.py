from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Organization, Storage


class StorageAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.org = Organization.objects.create(name="Test Organization")
        self.storage = Storage.objects.create(type="bio", capacity=1000, organization=self.org)


    def test_aboba(self):
        self.assertTrue(1 == 1)

    def test_create_storage(self):
        url = reverse('storage-list')
        data = {"type": "plastic", "capacity": 500, "organization": self.org.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_storage_capacity_limit(self):
        url = reverse('storage-detail', args=[self.storage.id])
        data = {"type": "bio", "capacity": 1500}  # Превышение capacity
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


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