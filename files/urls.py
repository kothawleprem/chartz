from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.filesHome, name='filesHome'),
    path(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)