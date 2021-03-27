from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    # path('home/',views.index, name='home'),
    path('charts/',views.charts,name='charts'),
    path('about/',views.about,name='about'),
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)