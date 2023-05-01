from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
	return render(request, 'tfc/plantas.html')

def pepino_page_view(request):
     return render(request, 'tfc/pepino.html')

def jardim_page_view(request):
	return render(request, 'tfc/omeujardim.html')

def definicoes_page_view(request):
    return render(request, 'tfc/definicoes.html')
