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
    path('planta/<int:planta_id>', views.planta_page_view, name = 'planta'),
    path('adicionar_planta/<int:planta_id>', views.adicionar_planta_view, name = 'adicionar'),
    path('adicionar_tratamento/<int:planta_cuidada_id>', views.adicionar_tratamento_page_view, name = 'adicionar_tratamento'),
    path('planta_cuidada/<int:planta_cuidada_id>', views.planta_cuidada_page_view, name = 'planta_cuidada'),
    path('omeujardim', views.jardim_page_view, name = 'omeujardim'),
    path('notificacoes', views.notificacoes_page_view, name = 'notificacoes'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)