from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("",auth, name="auth"),
    path("login",auth, name="auth"),
    path("langing",home, name="landing_page"),
    path("home/",home, name="landing_page"),
    path("about/",about, name="about"),
    path('contact/',contact),
    path('feeds/',feeds),
    path('blog/<slug:slug>/',viewblog, name="viewblog"),
    path('add_blog/',AddBlog, name="viewblog"),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
