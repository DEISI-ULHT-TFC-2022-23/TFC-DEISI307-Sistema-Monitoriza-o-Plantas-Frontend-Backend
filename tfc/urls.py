#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views

app_name = "tfc"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name = 'home')
]