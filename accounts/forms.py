from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=True)
    last_name = forms.CharField(label='Apellido', max_length=30, required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)
    birthday = forms.DateField(
        label='Fecha de cumpleaños',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    avatar = forms.ImageField(label='Avatar', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile, _ = Profile.objects.get_or_create(user=user)
            bday = self.cleaned_data.get('birthday')
            if bday:
                profile.birthday = bday
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                profile.avatar = avatar
            profile.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(
        label='Fecha de cumpleaños',
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'website', 'instagram', 'birthday')
        labels = {
            'avatar': 'Avatar',
            'bio': 'Bio',
            'website': 'Enlace',
            'instagram': 'Instagram',
            'birthday': 'Fecha de cumpleaños',
        }
        widgets = {
            'website': forms.URLInput(attrs={'placeholder': 'https://mi-sitio.com'}),
        }