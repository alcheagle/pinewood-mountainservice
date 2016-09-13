from django.http import HttpResponse
from django.shortcuts import render

from . import serializers
from . import models

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

def print_json(request, track_id):
    track = models.Track.objects.filter(_id=track_id)
    serializer = serializers.TrackSerializer(instance=track)

    return HttpResponse(JSONRenderer().render(serializer.data))
