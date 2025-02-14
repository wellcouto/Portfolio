from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from kdastro.models import Servidor
from .models import RemuneraServ, CobrancaServ
from .forms import EdicaoRemuneraServ
    
class ServidorView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Servidor
    context_object_name = 'servidores'
    paginate_by = 5
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Servidor.objects.all()
        if query:
            object_list = object_list.filter(
                Q(nome__icontains=query) | 
                Q(matricula__icontains=query))
        return object_list
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context
    

class RemuneracaoView(LoginRequiredMixin, ListView):
    template_name = 'competencias.html'
    model = RemuneraServ
    context_object_name = 'remuneraserv'
    
    def get_queryset(self):
        servidork = get_object_or_404(Servidor, pk=self.kwargs['pk'])
        return RemuneraServ.objects.filter(servidor_k=servidork)
    
class RemuneraCreateView(LoginRequiredMixin, CreateView):
    template_name = 'competencia_form.html'
    model = RemuneraServ
    context_object_name = 'crtremuneraserv'
    form_class = EdicaoRemuneraServ
    
    def get_success_url(self):
        return reverse_lazy('Remunera:competencias', kwargs={'pk': self.kwargs['pk']})


    def form_valid(self, form):
        form.instance.servidor_k_id = self.kwargs['pk']
        return super().form_valid(form)
        

class RemuneraUpdateView (LoginRequiredMixin, UpdateView):
    template_name = 'competencia_form.html'
    model = RemuneraServ
    context_object_name = 'upremuneraserv'
    form_class = EdicaoRemuneraServ
    
    def get_success_url(self):
        return reverse_lazy('Remunera:competencias', kwargs={'pk': self.object.servidor_k.pk})

class RemuneraDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'competencia_delete.html'
    model = RemuneraServ
    def get_success_url(self):
        return reverse_lazy('Remunera:competencias', kwargs={'pk': self.object.servidor_k.pk})

class VerificarMatriculaView(LoginRequiredMixin, TemplateView):
    template_name = 'verificar_matricula.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        matricula_existente = CobrancaServ.objects.filter(servidor_c__matricula=username).exists()

        if matricula_existente:
            context['mensagem'] = "Você está devendo X!"
        else:
            context['mensagem'] = "Você não está devendo"

        return context



class botpView(TemplateView):
    template_name = 'botp.html'
    