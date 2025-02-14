from django.contrib import admin
from .models import Funcionario, ItemNC, Atribuicao

admin.site.register(Funcionario)
admin.site.register(Atribuicao)
admin.site.register(ItemNC)
