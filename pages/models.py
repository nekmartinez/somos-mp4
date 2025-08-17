from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField('Título', max_length=200)
    subtitle = models.CharField('Subtítulo', max_length=250, blank=True)
    content = RichTextField('Contenido')
    image = models.ImageField('Imagen', upload_to='pages/', blank=True, null=True)
    link_url = models.URLField('Enlace (opcional)', blank=True, null=True)
    link_text = models.CharField('Texto del enlace', max_length=100, blank=True, default='')

    published_at = models.DateField('Fecha de publicación', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title