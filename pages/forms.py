
from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'content', 'image', 'link_url', 'link_text']
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'content': 'Contenido',
            'image': 'Imagen',
        }
