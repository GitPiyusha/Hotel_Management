from django.db import models

# Create your models here.
class HotelModel(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    rating = models.IntegerField()

def __str__(self):
    return self.name