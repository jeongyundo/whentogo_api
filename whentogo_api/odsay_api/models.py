from django.db import models

# Create your models here.

class Gpsdata(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sx = models.CharField(max_length=50)
    sy = models.CharField(max_length=50)
    ex = models.CharField(max_length=50)
    ey = models.CharField(max_length=50)
    opt = models.CharField(max_length=50)
    SearchType = models.CharField(max_length=50)
    SearchPathType = models.CharField(max_length=50)

    class Meta:
        ordering = ['created']
