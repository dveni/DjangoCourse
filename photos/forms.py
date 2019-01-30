from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS
from photos.validators import badwords_detector


class PhotoForm(forms.ModelForm):
    """
    Photo model form
    """
    class Meta:
        model = Photo
        exclude = ['owner']

