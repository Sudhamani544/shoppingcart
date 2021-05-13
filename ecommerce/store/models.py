from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.shortcuts import reverse
from django.db.models import Subquery, OuterRef

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

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
    # @property
    # def imageUrl(self):
    #     try:
    #         url=self.image.url
    #     except:
    #         url=''
    #     return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    # @property
    # def imageUrl(self):
    #     try:
    #         url=self.image.url
    #     except:
    #         url=''
    #     return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        print(self.orderitem_set.all())
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    fooditem = models.ForeignKey(FoodItems,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, default=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    dateadded = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.fooditem.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address
