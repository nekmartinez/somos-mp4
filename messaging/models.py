
from django.db import models
from django.contrib.auth.models import User
from pages.models import Page

class Comment(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField('Comentario')
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comentario de {self.author} en {self.page}'
