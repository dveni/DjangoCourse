
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet

# API Router
router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')


urlpatterns = [

    # API URLs
    re_path(r'1.0/', include(router.urls)),

]