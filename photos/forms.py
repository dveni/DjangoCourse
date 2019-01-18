from django import forms
from django.core.exceptions import ValidationError

from photos.models import Photo
from photos.settings import BADWORDS


class PhotoForm(forms.ModelForm):
    """
    Photo model form
    """
    class Meta:
        model = Photo
        exclude = ['owner']
    def clean(self):
        """
        Validate if in description there's badwords defined in settings.BADWORDS
        :return: dictionary with attributes if OK
        """

        cleaned_data = super(PhotoForm, self).clean()

        description = cleaned_data.get('description','').lower()

        for badword in BADWORDS:
            if badword.lower() in description:
                raise ValidationError('The word {0} is not allowed'.format(badword))

        return cleaned_data