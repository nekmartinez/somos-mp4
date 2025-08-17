from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UserUpdateForm, ProfileForm


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class UserLogoutView(LogoutView):
    next_page = 'home'
    http_method_names = ['get', 'post', 'head', 'options']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, 'Perfil actualizado.')
            return redirect('accounts:profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile_edit.html', {'uform': uform, 'pform': pform})


@login_required
def profile_detail(request, username):
    user_obj = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile_detail.html', {'profile_user': user_obj})


def _is_staff(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(_is_staff)
def user_list_admin(request):
    users = User.objects.all().order_by('-is_superuser', '-is_staff', 'username')
    return render(request, 'accounts/user_list.html', {'users': users})


@login_required
@user_passes_test(_is_staff)
@require_POST
def toggle_staff(request, pk):
    if str(request.user.pk) == str(pk):
        messages.error(request, 'No puedes cambiar tu propio estado de staff.')
        return redirect('accounts:user_list')

    u = get_object_or_404(User, pk=pk)
    u.is_staff = not u.is_staff
    u.save()

    if u.is_staff:
        messages.success(request, f'Staff concedido a {u.username}.')
    else:
        messages.warning(request, f'Staff revocado a {u.username}.')

    return redirect('accounts:user_list')


@login_required
@user_passes_test(_is_staff)
@require_POST
def toggle_superuser(request, pk):
    if str(request.user.pk) == str(pk):
        messages.error(request, 'No puedes cambiar tu propio estado de superusuario.')
        return redirect('accounts:user_list')
    u = get_object_or_404(User, pk=pk)
    u.is_superuser = not u.is_superuser
    u.is_staff = True if u.is_superuser else u.is_staff
    u.save()
    messages.success(request, f'Usuario {u.username}: is_superuser = {u.is_superuser}')
    return redirect('accounts:user_list')
