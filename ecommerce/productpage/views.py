from django.shortcuts import render
from store.models import FoodItems
from store import views
# Create your views here.

def chicken_pesto(request):
    item = FoodItems.objects.get(name='chicken_pesto')
    return render(request,'productpage/productpage.html', {'item' : item})

def margheritta(request):
    item = FoodItems.objects.get(name='margheritta')
    return render(request,'productpage/productpage.html', {'item' : item})

def mushroompizza(request):
    item = FoodItems.objects.get(name='mushroompizza')
    return render(request,'productpage/productpage.html', {'item' : item})
