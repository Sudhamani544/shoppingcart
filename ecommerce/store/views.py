from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
import json
# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = ['get_cart_total']

    fooditems = FoodItems.objects.all()
    context = {'fooditems': fooditems, 'cartItems':cartItems }
    return render(request,'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = ['get_cart_total']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}
        cartItems = ['get_cart_total']
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'store/checkout.html',context)

def updateitem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('action:',action)
    print('productId:',productId)

    customer = request.user.customer
    fooditem = FoodItems.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, fooditem=fooditem)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

# class StoreView(ListView):
#     model=FoodItems
#     template_name = "store/store.html"
