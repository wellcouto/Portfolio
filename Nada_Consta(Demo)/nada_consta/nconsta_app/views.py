from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Funcionario, ItemNC, Atribuicao
from .forms import EdicaoAtribuicaoForm, SignUpForm

@login_required
def home (request):
    return render(request, 'home.html')


@login_required   
def resultado_matricula(request):
    matricula = request.GET.get('matricula')
    funcionario = get_object_or_404(Funcionario, matricula=matricula)
    grupo_usuario = request.user.groups.first()
    atribuicao = get_object_or_404(Atribuicao, funcionario=funcionario, item__responsavel=grupo_usuario)
    
    if request.method == 'POST':
        form = EdicaoAtribuicaoForm(request.POST, instance=atribuicao)
        if form.is_valid():
            form.save()
            messages.info(request, 'Alteração Salva com Sucesso')        
    else:
        form = EdicaoAtribuicaoForm(instance=atribuicao)
            
    context = {'form': form, 'funcionario': funcionario, 'atribuicao': atribuicao,'grupo_usuario': grupo_usuario }     
    return render(request, 'resultado_busca.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Caso o login não seja bem sucedido, pode-se retornar uma mensagem de erro.
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    else:
        return render(request, 'login.html')

# @login_required   
# def redirectsepag (request):
#     if request.user.groups.filter(name='SEPAG').exists():
#         return redirect ('sepag')
#     else:
#         return redirect ('home')

@login_required
def sepag (request):
    matricula = request.GET.get('matricula')
    funcionario = get_object_or_404(Funcionario, matricula=matricula)
    atribuicoes = Atribuicao.objects.filter(funcionario=funcionario)
            
    context = {'funcionario': funcionario, 'atribuicoes': atribuicoes} 
    return render(request, 'sepag.html', context)

@login_required   
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')



#def edicao_nadaconsta (request, resultado):
    objeto = Servidor.objects.get(matricula=resultado)
    
    if request.method == 'POST':
        cargo_att = request.POST.get ('cargo')
        situacao_att = request.POST.get ('situacao')
        
        objeto.cargo = cargo_att
        objeto.situacao = situacao_att
        objeto.save(force_update=True)
        return redirect ('resultado-matricula')
    
    return render (request, 'resultado_busca.html', {'objeto':objeto})