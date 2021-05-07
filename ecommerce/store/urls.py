from django.urls import path
from . import views


urlpatterns = [
    path('',views.StoreView.as_view(),name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
#     path('addtocart/',views.addtocart,name='addtocart'),
]
