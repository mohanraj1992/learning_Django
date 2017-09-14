# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    #commented out are old methods of creating
    #html = ''
    #for album in all_albums:
    #    url = '/music/' + str(album.id) + '/'
    #    html += '<a href="'+url+'">'+album.album_title + '</a><br>'
    #return HttpResponse(html)

    #Below changes are made for tutorial 15
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)




def detail(request, album_id):

    #this is for old
    #return HttpResponse("<h2>Details for Album id:" + str(album_id) + "</h2>")

    # below is covered on tutorial 16
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not eist")
    return render(request,'music/detail.html', {'album': album})