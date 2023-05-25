from django import forms
from django.forms import ModelForm

from .models import Tratamento

class TratamentoForm(ModelForm):
    class Meta:
        model = Tratamento
        fields = "__all__"
        exclude = ['planta_cuidada']