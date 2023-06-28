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
    dias = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    agua = [0.1, 4.2, 3.3, 1.9, 0.8, 4.1, 3.1, 1.0, 4.2, 3.4, 2.0, 0.6, 4.1, 3.0, 1.6, 0.3, 4.2, 3.5, 2.1, 0.7, 4.2, 3.7, 2.5, 1.2, 0.2, 4.0, 3.4, 2.8, 1.9, 1.0, 4.2]
    plt.plot(dias,agua)

    plt.title('Quantidade de Água da planta "Roseira" durante o mês de maio')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade de Água (litros)')
    plt.show()

    dias2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    agua2 = [20.2, 20.2, 10.3, 20.2, 10.3, 20.1, 10.3, 20.0, 10.3, 20.2, 10.3, 20.2, 10.3, 20.2, 10.3, 20.2, 10.3, 20.1, 10.1, 20.0, 10.2, 20.2, 10.5, 19.9, 9.9, 20.1, 10.3, 20.2, 10.3, 20.2, 10.3]
    plt.plot(dias2,agua2)

    plt.title('Quantidade de Água da planta "Abacateiro" durante o mês de maio')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade de Água (litros)')
    plt.show()

    return render(request, 'tfc/agua.html')


def fertilizante_page_view(request):
    dias = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    fertilizante = [0.2, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 1.9, 1.8, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6]
    plt.plot(dias,fertilizante)

    plt.title('Quantidade de Fertilizantes na planta "Roseira" durante o mês de maio')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade de Fertilizantes (Quilos)')
    plt.show()


    dias2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    fertilizante2 = [0.4, 1.4, 1.4, 1.4, 1.3, 1.3, 1.3, 1.2, 1.2, 1.2, 1.2, 1.2, 1.1, 1.1, 1.0, 1.0, 0.9, 0.9, 0.8, 0.8, 0.7, 0.6, 0.5, 1.4, 1.4, 1.4, 1.3, 1.2, 1.1, 1.0, 1.0]
    plt.plot(dias2,fertilizante2)

    plt.title('Quantidade de Fertilizantes na planta "Abacateiro" durante o mês de maio')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade de Fertilizantes (Quilos)')
    plt.show()

    return render(request, 'tfc/fertilizante.html')

def curiosidade_page_view(request):
    return render(request, 'tfc/curiosidade.html')


def curiosidade2_page_view(request):
    return render(request, 'tfc/curiosidade2.html')


def inicio_page_view(request):
    return render(request, 'tfc/inicio.html')

def meteorologia_page_view(request):
    return render(request,'tfc/meteorologia.html')


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
