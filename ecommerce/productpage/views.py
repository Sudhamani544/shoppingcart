from django.shortcuts import render
from store.models import FoodItems, Pictures
from store import views
# Create your views here.

def chicken_pesto(request):
    item = FoodItems.objects.get(name='chicken_pesto')
    img = Pictures.objects.get(name='chicken_pesto')
    return render(request,'productpage/productpage.html', {'item' : item, 'img' : img })

def margheritta(request):
    item = FoodItems.objects.get(name='margheritta')
    img = Pictures.objects.get(name='margheritta')
    return render(request,'productpage/productpage.html', {'item' : item, 'img' : img })

def mushroompizza(request):
    item = FoodItems.objects.get(name='mushroompizza')
    img = Pictures.objects.get(name='mushroompizza')
    return render(request,'productpage/productpage.html', {'item' : item, 'img' : img })
