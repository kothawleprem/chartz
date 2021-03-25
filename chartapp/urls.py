from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.index, name='home'),
    path('charts/',views.charts,name='charts'),
    path('about/',views.about,name='about'),
 
]