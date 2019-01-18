from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from photos.forms import PhotoForm
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

@login_required()
def create(request):
    """
    Shows a form to create a pic and creates it if POST
    :param request: HttpRequest
    :return: HttpResponse
    """

    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()

    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()
            success_message = 'Pic created successfully! '
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'See pic'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)