from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ItemNC, Funcionario, Atribuicao

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
class EdicaoAtribuicaoForm(forms.ModelForm):
    class Meta:
        model = Atribuicao
        fields = ['status_item']
        