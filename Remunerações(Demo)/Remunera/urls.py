from django.urls import path
from Remunera.views import ServidorView, RemuneracaoView,RemuneraCreateView, RemuneraUpdateView, RemuneraDeleteView, VerificarMatriculaView, botpView

app_name = "Remunera"

urlpatterns = [
    path('home/', ServidorView.as_view(), name = "home"),
    path('servidor/<int:pk>/competencias', RemuneracaoView.as_view(), name="competencias"),
    path('servidor/<int:pk>/competencias/nova/', RemuneraCreateView.as_view(), name='competencia_criar'),
    path('competencias/<int:pk>/editar/', RemuneraUpdateView.as_view(), name='competencia_editar'),
    path('competencias/<int:pk>/delete/', RemuneraDeleteView.as_view(), name='competencia_deletar'),
    path('verificarmatricula/', VerificarMatriculaView.as_view(), name = "verificarmatricula"),
    path('bootstrapd/', botpView.as_view(), name='bootstrapd'),

]