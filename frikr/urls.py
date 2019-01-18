"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from photos.views import HomeView, DetailView, CreateView
from users.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),

    # photos URLs
    re_path('^$', HomeView.as_view(), name='photos_home'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    re_path(r'^photos/new$', CreateView.as_view(), name='create_photo'),

    # Users URLs
    re_path(r'^login$', LoginView.as_view(), name='users_login'),
    re_path(r'^logout$', LogoutView.as_view(), name='users_logout')
]
