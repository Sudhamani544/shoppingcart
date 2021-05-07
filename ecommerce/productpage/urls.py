from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/',views.ItemDetailView.as_view(),name='product'),
    # path('margherita/',views.margherita,name="margherita"),
    # path('mushroompizza/',views.mushroompizza,name="mushroompizza"),
    # path('chicken_pesto/',views.chicken_pesto,name="chicken_pesto"),
]
