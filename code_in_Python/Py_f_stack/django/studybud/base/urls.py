from django.urls import path  ## So that we cpecify paths
from . import views

urlpatterns = [
    path('',views.home_page, name="home"),
    path('rooms/',views.rooms,name="rooms"),
]