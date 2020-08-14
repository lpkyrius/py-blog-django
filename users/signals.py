# signals um tipo de gatilhos
# post_save é disparado após um objeto ser salvo
# User is the sender
# And the receiver que vai executar
# e o profile já que vamos criar um profile

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# função que será executada, sempre que um User for criado e ela criará o Profile default para ele.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# agora a função para salvar o profile quando for salvo normalmente
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
