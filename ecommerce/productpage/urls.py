from django.urls import path
from . import views

urlpatterns = [
    path('margheritta/',views.margheritta,name="margheritta"),
    path('mushroompizza/',views.mushroompizza,name="mushroompizza"),
    path('chickenpesto/',views.chickenpesto,name="chickenpesto"),
]
