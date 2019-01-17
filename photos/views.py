from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from photos.models import Photo, PUBLIC


def home(request):
    """
    :param request:
    :return: Home page of Photos
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')

    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Load details page of a pic
    :param request: HttpRequest
    :param pk: pic id
    :return: HttpResponse
    """

    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) == 1 else None
    if photo is not None:
        context = {
            'photo': photo
        }
        return render(request,'photos/detail.html',context)
    else:
        return HttpResponseNotFound('Pic does not exist :(')