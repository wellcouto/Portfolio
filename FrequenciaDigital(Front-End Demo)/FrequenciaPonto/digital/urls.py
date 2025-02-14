from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mes/', views.mes, name='mes'),
    path('mes_anterior/', views.meses_anteriores, name="mes_anterior"),
    path('ferias_afastamentos', views.ferias, name='ferias'),
    path('user/', views.user, name='user'),
    path('gestao/', views.gestao, name='gestao'),
]