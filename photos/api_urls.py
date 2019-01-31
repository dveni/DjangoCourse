from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from photos.api import PhotoViewSet

# API Router
router = DefaultRouter()
router.register(r'photos', PhotoViewSet)


urlpatterns = [
    # API URLs
    re_path(r'1.0/', include(router.urls)),
]