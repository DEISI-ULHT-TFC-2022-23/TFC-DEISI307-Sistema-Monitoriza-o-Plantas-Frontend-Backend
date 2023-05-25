from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Planta)
admin.site.register(Utilizador)
admin.site.register(PlantaCuidada)
admin.site.register(Tratamento)
admin.site.register(Monitorizacao)