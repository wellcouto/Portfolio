from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('resultado/', views.resultado_matricula, name='resultado-matricula'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('sepag/', views.sepag, name='sepag'),
    #path('redirectsepag/', views.redirectsepag, name='redirectsepag'),

    
    #path('editar_atribuicao/<int:atribuicao_id>/', views.editar_atribuicao, name='editar_atribuicao'),
]