from rest_framework import serializers

from .models import Organization, Storage


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['name', 'bio_waste', 'glass', 'plastic']

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['name', 'bio_waste_capacity', 'glass_capacity', 'plastic_capacity', 'latitude', 'longitude']
