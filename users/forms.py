from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    # já herdei tudo do UserCreationForm
    # agora vamos adicionar os nossos campos
    email = forms.EmailField() # required=false default=true

    class Meta:
        # ao final criará um User, ou seja, o model será o User
        model = User
        # lista dos campos que desejo exibir
        fields = ['username', 'email', 'password1', 'password2']

# para atulizar os campos do profile baseado no user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# para atualizar a imagem
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
