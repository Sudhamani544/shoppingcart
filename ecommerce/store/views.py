from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
# Create your views here.

class StoreView(ListView):
    model=FoodItems
    template_name = "store/store.html"

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
    context = {'items':items, 'order':order}
    return render(request,'store/checkout.html',context)

# def store(request):
#     items = FoodItems.objects.all()
#     return render(request,'store/store.html', {'items' : items})

