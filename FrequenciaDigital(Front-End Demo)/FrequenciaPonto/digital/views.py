from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def mes(request):
    return render(request,'mes.html')

def ferias(request):
    return render(request, 'ferias.html')

def user(request):
    return render(request, 'user.html')

def meses_anteriores(request):
    return render(request, 'mes_anterior.html')

def voltar(request):
    return render(request, 'voltar.html')

def gestao(request):
    return render(request, 'gestao.html')