from .import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('api/get-hotels',views.get_hotel)
 
]