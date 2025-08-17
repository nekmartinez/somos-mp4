from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, UserPasswordChangeView, UserPasswordChangeDoneView,
    signup, profile, profile_edit, profile_detail, user_list_admin, toggle_staff, toggle_superuser
)

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/', profile, name='profile'),
    path('password/change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('users/', user_list_admin, name='user_list'),
    path('users/<int:pk>/toggle-staff/', toggle_staff, name='toggle_staff'),
    path('users/<int:pk>/toggle-superuser/', toggle_superuser, name='toggle_superuser'),
    path('profile/<str:username>/', profile_detail, name='profile_detail'),
]