from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # para redefinir o tam da imagem do profile eu sobreponho a função save com algumas funcionalidades
    # importante para a performance do site (para não ficar carregando imagens grandes o tempo todo)
    # rodará após o módulo save ser executado.
    # é uma forma de sobrescrever o método save() de um model
    # def save(self):
    def save(self, *args, **kawrgs):
        # Rodar a função SAVE da classe mãe
        # super().save()
        super().save(*args, **kawrgs)

        # pega a imagem para redimencionar
        img = Image.open(self.image.path)

        # verifica se a imagem é maior que o desejado
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
