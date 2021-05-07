from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodItems
from django.views.generic import ListView, DetailView
# Create your views here.

class StoreView(ListView):
    model=FoodItems
    template_name = "store/store.html"

def cart(request):
    context = {}
    return render(request,'store/cart.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
