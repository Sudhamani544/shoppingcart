from django.urls import path
from . import views

urlpatterns = [
    path('margheritta/',views.margheritta,name="margheritta"),
    path('mushroompizza/',views.mushroompizza,name="mushroompizza"),
    path('chicken_pesto/',views.chicken_pesto,name="chicken_pesto"),
]
