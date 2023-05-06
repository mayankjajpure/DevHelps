from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",home, name="landing_page"),
    path("home/",home, name="landing_page"),
    path("about/",about, name="about"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
