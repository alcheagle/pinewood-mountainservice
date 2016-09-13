from django.db import models

class Position(models.Model):
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    elevation = models.DecimalField()
    
    def __str__(self):
        return "(latitude: {}, longitude: {}, altitude: {})".format(self.latitude, self.longitude, self.elevation)

class Segment(models.Model):
    begin = models.OneToOneField(Position, on_delete=models.CASCADE)
    end = models.OneToOneField(Position, on_delete=models.CASCADE)
    
    def __str__(self):
        return "(begin: {}, end: {})".format(self.begin, self.end)

class Track(models.Model):
    _id = models.charField(max_length=10)
    descr = models.charfield(max_length=200)
    tracks = models.ManyToManyField(Segment)

    def __str__(self):
        return self._id
