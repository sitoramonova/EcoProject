from geopy.distance import geodesic
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Organization, Storage
from .serializers import OrganizationSerializer, StorageSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        organization = serializer.save()

class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

    def get_nearest_storage(self, latitude, longitude, waste_type, amount):
        storage_list = Storage.objects.all()
        closest_storage = None
        closest_distance = float('inf')
        for storage in storage_list:
            if storage.can_accept(waste_type, amount):
                distance = geodesic((latitude, longitude), (storage.latitude, storage.longitude)).km
                if distance < closest_distance:
                    closest_distance = distance
                    closest_storage = storage
        return closest_storage

    def transfer_waste(self, organization_id, waste_type, amount):
        organization = Organization.objects.get(id=organization_id)
        latitude, longitude = organization.latitude, organization.longitude
        nearest_storage = self.get_nearest_storage(latitude, longitude, waste_type, amount)
        if nearest_storage:
            return Response({"storage": nearest_storage.name, "distance": nearest_storage.distance})
        else:
            return Response({"error": "No suitable storage found"}, status=400)
