from django.core.exceptions import ValidationError

from photos.settings import BADWORDS


def badwords_detector(value):
    """
    Validate if there's badwords defined in settings.BADWORDS
    :return: Boolean
    """

    for badword in BADWORDS:
        if badword.lower() or badword in value:
            raise ValidationError('The word {0} is not allowed'.format(badword))

    return True