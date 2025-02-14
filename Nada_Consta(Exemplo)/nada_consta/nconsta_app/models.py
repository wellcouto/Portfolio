from django.db import models
from django.contrib.auth.models import Group, User

class ItemNC(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=30, null=True)
    # Outros campos relevantes para o item

    def __str__(self):
        return self.nome
    
    
class Funcionario(models.Model):
    matricula = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    situacao = models.CharField(max_length=50)
    setor = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    itens_atribuidos = models.ManyToManyField(ItemNC, through='Atribuicao')
    # Outros campos relevantes do funcionário

    def __str__(self):
        return self.matricula

class Atribuicao(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemNC, on_delete=models.CASCADE)
    status_item = models.BooleanField(default= False)
    # Outros campos, como informações específicas da atribuição

    def __str__(self):
        return f"{self.funcionario.nome} - {self.item.nome}"
