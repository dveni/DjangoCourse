from django.contrib.auth.decorators import login_required
from django.urls import re_path, include
from photos.views import HomeView, DetailView, CreateView, PhotoListView, UserPhotosView

urlpatterns = [

    # photos URLs
    re_path('^$', HomeView.as_view(), name='photos_home'),
    re_path('^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'),
    re_path('^photos/$', PhotoListView.as_view(), name='photos_list'),
    re_path(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'),
    re_path(r'^photos/new$', CreateView.as_view(), name='create_photo'),
]