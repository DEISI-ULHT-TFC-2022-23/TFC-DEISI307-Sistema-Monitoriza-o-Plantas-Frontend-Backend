from django.contrib import admin

from .models import Condicao, Planta, Utilizador

# Register your models here.

admin.site.register(Condicao)
admin.site.register(Planta)
admin.site.register(Utilizador)