
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet
from users.views import LoginView, LogoutView

urlpatterns = [

    # Users URLs
    re_path(r'^login$', LoginView.as_view(), name='users_login'),
    re_path(r'^logout$', LogoutView.as_view(), name='users_logout'),

]
