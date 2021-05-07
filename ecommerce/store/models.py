from django.db import models
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse

# Create your models here.
class FoodItems(models.Model):
    name  = models.CharField(max_length=100)
    image = CloudinaryField('image')
    desc  = models.TextField()
    price = models.IntegerField()
    piece = models.IntegerField()
    offer = models.BooleanField(default=False)
    discountprice = models.IntegerField(blank=True, null=True)
    slug  = models.SlugField()
    def __str__(self):
        return self.name
