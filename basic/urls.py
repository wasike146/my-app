from operator import index
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='main'),
    path('room/', views.room,name='room'),
]