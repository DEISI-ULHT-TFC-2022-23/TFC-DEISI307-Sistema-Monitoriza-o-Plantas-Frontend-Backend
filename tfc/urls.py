#  hello/urls.py

from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "tfc"

urlpatterns = [
    path('seu_endpoint/', views.seu_endpoint, name='seu_endpoint'),
    
    path('', views.splashscreen_view, name = 'splashscreen'),
    path('splashscreen', views.splashscreen_view, name = 'splashscreen'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('dashboard', views.dashboard_page_view, name = 'dashboard'),
    path('agua', views.agua_page_view, name = 'agua'),
    path('fertilizante', views.fertilizante_page_view, name = 'fertilizante'),

    path('inicio', views.inicio_page_view, name = 'inicio'),
    path('meteorologia', views.meteorologia_page_view, name='meteorologia'),
    path('curiosidade', views.curiosidade_page_view, name = 'curiosidade'),
    path('curiosidade2', views.curiosidade2_page_view, name = 'curiosidade2'),

    path('plantas', views.plantas_page_view, name = 'plantas'),
    path('planta/<int:planta_id>', views.planta_page_view, name = 'planta'),
    path('adicionar_planta/<int:planta_id>', views.adicionar_planta_view, name = 'adicionar'),
    
    path('omeujardim', views.jardim_page_view, name = 'omeujardim'),
    path('adicionar_tratamento/<int:planta_cuidada_id>', views.adicionar_tratamento_page_view, name = 'adicionar_tratamento'),
    path('apagar/<int:planta_cuidada_id>', views.apaga_planta_cuidada_view, name = 'apagar'),
    path('planta_cuidada/<int:planta_cuidada_id>', views.planta_cuidada_page_view, name = 'planta_cuidada'),
    path('notificacoes', views.notificacoes_page_view, name = 'notificacoes'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)