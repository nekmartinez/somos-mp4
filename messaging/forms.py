
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribí tu comentario…'})}
        labels = {'body': 'Comentario'}
