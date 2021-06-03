from django.shortcuts import render
from django.http import HttpResponse

from .models import Artist, Album, Track


# Create your views here.
def index(request):
    artists_list = Artist.objects.all()
    albums_list = Album.objects.all()
    tracks_list = Track.objects.all()
    return render(request, 'index.html', {
        'artists_list': artists_list,
        'albums_list': albums_list,
        'tracks_list': tracks_list
    })
