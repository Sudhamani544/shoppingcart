from django.shortcuts import render
from .models import FoodItems, Pictures
# Create your views here.

def store(request):
    items = FoodItems.objects.all()
    images = Pictures.objects.all()
    return render(request,'store/store.html', {'items' : items, 'images':images})

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
