from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TratamentoForm
from django.shortcuts import redirect
from .models import *
import matplotlib.pyplot as plt


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username = username,
            password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('tfc:dashboard'))
        else:
            return render(request, 'tfc/login.html', {
                'message': 'Credenciais inválidas! Tente Novamente.'
            })

    return render(request, 'tfc/login.html')

def logout_view(request):
    logout(request)

    return render(request, 'tfc/login.html', {
                'message': 'Foi desconectado.'
            })


def splashscreen_view(request):
	return render(request, 'tfc/splashscreen.html')


def dashboard_page_view(request):
    #meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
    #valores = [105235, 107697, 110256, 109236, 108859, 109986]
    #plt.plot(meses,valores)
    #plt.show()

    return render(request, 'tfc/dashboard.html')


def inicio_page_view(request):

    context = {}
    return render(request, 'tfc/inicio.html')


def plantas_page_view(request):
    plantas = Planta.objects.all()
    context = {'plantas' : plantas}

    return render(request, 'tfc/plantas.html', context)


def planta_page_view(request, planta_id):
    planta = Planta.objects.get(pk = planta_id)
    context = {'planta' : planta}

    return render(request, 'tfc/planta.html', context)


def adicionar_planta_view(request, planta_id):
    planta = Planta.objects.get(pk = planta_id)
    user = Utilizador.objects.get(nome = "Pedro")
    planta_cuidade = PlantaCuidada.objects.create(
         planta = planta,
         utilizador = user
    )

    return redirect('tfc:plantas')


def planta_cuidada_page_view(request, planta_cuidada_id):
    planta_cuidada = PlantaCuidada.objects.get(pk = planta_cuidada_id)
    tratamentos = Tratamento.objects.filter(planta_cuidada = planta_cuidada)
    context = {
        'planta_cuidada' : planta_cuidada, 
        'tratamentos' : tratamentos
    }

    return render(request, 'tfc/planta_cuidada.html', context)


def jardim_page_view(request):
    user = Utilizador.objects.get(nome = "Pedro")
    plantas_cuidadas = PlantaCuidada.objects.filter(
        utilizador = user
    )

    context = {'plantas_cuidadas' : plantas_cuidadas}

    return render(request, 'tfc/omeujardim.html', context)


def adicionar_tratamento_page_view(request, planta_cuidada_id):
    planta_cuidada = PlantaCuidada.objects.get(pk = planta_cuidada_id)
    form = TratamentoForm()

    context = {
        'planta_cuidada' : planta_cuidada, 
        'form' : form
    }

    return render(request, 'tfc/tratamento.html', context)


def notificacoes_page_view(request):
    return render(request, 'tfc/notificacoes.html')
