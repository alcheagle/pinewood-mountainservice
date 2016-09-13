from django.db import models

class Position(models.Model):
    latitude = models.DecimalField(max_digits=18, decimal_places=18)
    longitude = models.DecimalField(max_digits=18, decimal_places=18)
    elevation = models.DecimalField(max_digits=18, decimal_places=18)
    
    def __str__(self):
        return "(latitude: {}, longitude: {}, altitude: {})".format(self.latitude, self.longitude, self.elevation)

class Segment(models.Model):
    begin = models.OneToOneField(Position, on_delete=models.CASCADE, related_name="begin")
    end = models.OneToOneField(Position, on_delete=models.CASCADE, related_name="end")
    
    def __str__(self):
        return "(begin: {}, end: {})".format(self.begin, self.end)

class Track(models.Model):
    _id = models.CharField(max_length=10)
    descr = models.CharField(max_length=200)
    tracks = models.ManyToManyField(Segment)

    def __str__(self):
        return self._id
