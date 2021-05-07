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

    # def get_absolute_url(self):
    #     return reverse("store:product",kwargs={
    #     'slug': self.slug
    #     })
#
# class OrdItem(models.Model):
# #     # user= models.ForeignKey(User,on_delete=models.CASCADE)
# #     # ordered = models.BooleanField(default = False)
#     fooditem = models.ForeignKey(FoodItems,on_delete=models.CASCADE)
# #     # quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return 'f"{self.quantity} of {self.item.name}"'
#
# class Order(models.Model):
#     user= models.ForeignKey(User,on_delete=models.CASCADE)
#     items=models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add = True )
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default = False)
#
#     def __str__():
#         return self.user.username
