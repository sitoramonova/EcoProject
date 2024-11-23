from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OrganizationViewSet, StorageViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'storage', StorageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
