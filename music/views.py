# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404
from django.http import HttpResponse
from .models import Album #data
from django.template import loader
# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except:
        raise Http404("沒有這張專輯喔")
    return render(request, 'music/detail.html', {'album': album, 'artist': album.artist})
