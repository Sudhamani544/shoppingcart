from django.shortcuts import render
from store.models import FoodItems
from store import views
from django.views.generic import ListView, DetailView
# Create your views here.

class ItemDetailView(DetailView):
    model = FoodItems
    template_name = 'productpage/productpage.html'

# def chicken_pesto(request):
#     item = FoodItems.objects.get(name='chicken_pesto')
#     # img = Pictures.objects.get(name='chicken_pesto')
#     return render(request,'productpage/productpage.html', {'item' : item})
#
# def margherita(request):
#     item = FoodItems.objects.get(name='margherita')
#     # img = Pictures.objects.get(name='margheritta')
#     return render(request,'productpage/productpage.html', {'item' : item})
#
# def mushroompizza(request):
#     item = FoodItems.objects.get(name='mushroompizza')
#     # img = Pictures.objects.get(name='mushroompizza')
#     return render(request,'productpage/productpage.html', {'item' : item })
