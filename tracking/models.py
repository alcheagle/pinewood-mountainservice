from django.db import models

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    #latitude = models.DecimalField(max_digits=18, decimal_places=18)
    #longitude = models.DecimalField(max_digits=18, decimal_places=18)
    #elevation = models.DecimalField(max_digits=18, decimal_places=18)
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    elevation = models.CharField(max_length=40)

    class Meta:
        unique_together = ("latitude", "longitude", "elevation")
    
    def __str__(self):
        return "(latitude: {}, longitude: {}, altitude: {})".format(self.latitude, self.longitude, self.elevation)

    def save():
        if not self.objects.filter(latitude=latitude, longitude=longitude, elevation=elevetion).exists():
            super(models.Model, self).save()

class Segment(models.Model):
    id = models.AutoField(primary_key=True)
    begin = models.OneToOneField(Position, on_delete=models.CASCADE, related_name="begin")
    end = models.OneToOneField(Position, on_delete=models.CASCADE, related_name="end")
    
    class Meta:
        unique_together = ("begin", "end")

    def __str__(self):
        return "(begin: {}, end: {})".format(self.begin, self.end)
    
    def save():
        if not self.objects.filter(begin=begin, end=end).exists():
            super(models.Model, self).save()

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    #name = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10, unique=True)
    descr = models.CharField(max_length=200)
    tracks = models.ManyToManyField(Segment)
    #TODO add boundaries field

    def __str__(self):
        return str(self.id)

    def save():
        if not self.objects.filter(name=name).exists():
            super(models.Model, self).save()
