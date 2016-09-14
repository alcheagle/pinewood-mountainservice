from rest_framework import serializers
from tracking.models import *

class PositionSerializer(serializers.Serializer):    

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

class SegmentSerializer(serializers.Serializer):
    begin = PositionSerializer(many=False, read_only=True)
    end = PositionSerializer(many=False, read_only=True)

    def create(self, validated_data):
        return Segment.objects.create(**validated_data)

class TrackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10,)
    descr = serializers.CharField(max_length=200,)
    tracks = SegmentSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Track.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance._id = validated_data.get('_id', instance._id)
        instance.descr = validated_data.get('descr', instance.descr)
        instance.tracks = validated_data.get('tracks', instance.tracks)
        instance.save()

        return instance
        
