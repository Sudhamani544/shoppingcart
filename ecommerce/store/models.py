from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class FoodItems(models.Model):
    name  = models.CharField(max_length=100)
    # image = CloudinaryField('image')
    desc  = models.TextField()
    price = models.IntegerField()
    piece = models.IntegerField()
    offer = models.BooleanField(default=False)

class Pictures(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
