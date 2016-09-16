from django.http import HttpResponse
from django.shortcuts import render

from . import serializers
from . import models

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def print_json(request, track_id):
    track = models.Track.objects.filter(name=track_id)

    if track.exists():
        serializer = serializers.TrackSerializer(instance=track[0])
        print(serializer)
        return HttpResponse(JSONRenderer().render(serializer.data),  content_type="application/json")
    else:
        return HttpResponse("Fail")
    
    #print(serializer.data)

