from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField('Avatar', upload_to='avatars/', blank=True, null=True)
    bio = models.TextField('Bio', blank=True)
    website = models.URLField('Sitio web', blank=True)
    instagram = models.CharField('Instagram', max_length=100, blank=True)
    birthday = models.DateField('Fecha de cumpleaños', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return f'Perfil de {self.user.username}'


@receiver(post_save, sender=User)
def create_profile_only_on_user_creation(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
