from django.db import models
from kdastro.models import Servidor

class RemuneraServ(models.Model):
    servidor_k = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    competencia = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.servidor_k.matricula} - {self.servidor_k.nome} - {self.competencia}"

class CobrancaServ(models.Model):
    servidor_c = models.ForeignKey(Servidor, on_delete=models.CASCADE)
    valor_devido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.servidor_c.matricula} - {self.servidor_c.nome} - {self.valor_devido}"

# Create your models here.
