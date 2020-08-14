from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

'''
-------------------------------------------------------
O próprio Django faz as tratativas com o banco de dados
Assim posso mudar o banco sem precisar alterar o código
As tabelas são tratadas como Classes
E os campos como atributos destas classes
-------------------------------------------------------
'''
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() # texto ilimitado
    '''
    opções de data automática, mas não permite alteração
    ----------------------------------------------------
    date_posted = models.DateTimeField(auto_now=True) # data de criação/update
    date_posted = models.DateTimeField(auto_now_add=True) # data de criação
    '''
    date_posted = models.DateTimeField(default=timezone.now) # now sem travar alterações
    # agora informo que o cmapo author será chave 1 para N para isso
    # informo ForeignKey e passo 2 parâmetros: User - para pegar dessa tabela
    # e on_delete para integridade (se deletar o usuário, deleta seus posts)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
