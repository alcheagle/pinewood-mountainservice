from django.http import HttpResponse
from django.shortcuts import render

from . import serializers
from . import models

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def print_json(request, track_id):
    track = models.Track.objects.filter(name=track_id)
    print(track.values())
    #serializer = serializers.TrackSerializer(instance=track.values())
    #print(serializer)
    
    #print(serializer.data)

    #return HttpResponse(JSONRenderer().render(serializer.data))
    return HttpResponse("ok")
