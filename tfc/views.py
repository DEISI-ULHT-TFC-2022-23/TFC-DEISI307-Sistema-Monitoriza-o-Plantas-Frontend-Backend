from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import TratamentoForm
from django.shortcuts import redirect
from .models import *
import matplotlib.pyplot as plt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def seu_endpoint(request):
    if request.method == 'POST':
        try:
            # Recebe o JSON da solicitação POST
            json_data = json.loads(request.body)
            
            # Faça o processamento necessário com os dados do JSON
            # Aqui está um exemplo de como você pode acessar os valores:
            chave1 = json_data['chave1']
            chave2 = json_data['chave2']
            chave3 = json_data['chave3']
            chave4 = json_data['chave4']
            chave5 = json_data['chave5']
            
            # Realize as operações desejadas com os dados recebidos
            
            # Retorna uma resposta JSON de sucesso
            response_data = {'success': True}
            return JsonResponse(response_data)
        
        except json.JSONDecodeError:
            # Retorna uma resposta JSON com erro se o JSON for inválido
            response_data = {'success': False, 'error': 'JSON inválido'}
            return JsonResponse(response_data, status=400)
    else:
        # Retorna uma resposta JSON com erro se o método da solicitação não for POST
        response_data = {'success': False, 'error': 'Método não permitido'}
        return JsonResponse(response_data, status=405)


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
    return render(request, 'tfc/dashboard.html')


def agua_page_view(request):
    meses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    valores = [105235, 107697, 110256, 109236, 108859, 109986, 109236, 109236,105235, 107697, 110256, 109236, 108859, 109986, 109236, 109236,105235, 107697, 110256, 109236, 108859, 109986, 109236, 109236,105235, 107697, 110256, 109236, 108859, 109986, 109236]
    plt.plot(meses,valores)

    plt.title('Quantidade de Água da planta X durante o mês de maio')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade de Água')
    plt.show()

    return render(request, 'tfc/agua.html')


def fertilizante_page_view(request):
    #meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
    #valores = [105235, 107697, 110256, 109236, 108859, 109986]
    #plt.plot(meses,valores)
    #plt.show()

    return render(request, 'tfc/fertilizante.html')

def curiosidade_page_view(request):
    return render(request, 'tfc/curiosidade.html')


def curiosidade2_page_view(request):
    return render(request, 'tfc/curiosidade2.html')


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
    form = TratamentoForm(request.POST or None)

    if request.method == 'POST':
        Tratamento.objects.create(
            planta_cuidada = planta_cuidada,
            quantidade_agua = request.POST ['quantidade_agua'],
            quantidade_fertilizante = request.POST ['quantidade_fertilizante'],
        )

    context = {
        'planta_cuidada' : planta_cuidada, 
        'form' : form
    }

    return render(request, 'tfc/tratamento.html', context)


def apaga_planta_cuidada_view(request, planta_cuidada_id):
    PlantaCuidada.objects.get(pk = planta_cuidada_id).delete()

    return redirect('tfc:omeujardim')


def notificacoes_page_view(request):
    return render(request, 'tfc/notificacoes.html')
