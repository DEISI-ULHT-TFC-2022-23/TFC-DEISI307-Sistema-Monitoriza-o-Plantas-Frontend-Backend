#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "tfc"

urlpatterns = [
    path('', views.splashscreen_view, name = 'splashscreen'),
    path('splashscreen', views.splashscreen_view, name = 'splashscreen'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('dashboard', views.dashboard_page_view, name = 'dashboard'),
    path('inicio', views.inicio_page_view, name = 'inicio'),
    path('plantas', views.plantas_page_view, name = 'plantas'),
    path('omeujardim', views.jardim_page_view, name = 'omeujardim'),
    path('definicoes', views.definicoes_page_view, name = 'definicoes'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)