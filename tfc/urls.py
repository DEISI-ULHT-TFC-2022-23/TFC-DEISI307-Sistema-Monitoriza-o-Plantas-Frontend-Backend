#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "tfc"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name = 'home'),
    path('about', views.about_page_view, name = 'about')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)