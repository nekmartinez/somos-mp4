from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def username_with_badge(user):
    """
    Uso en templates:
      {% load user_extras %}
      {% username_with_badge user %}
    """
    if not user:
        return ""
    if getattr(user, "is_superuser", False) or getattr(user, "is_staff", False):
        return format_html('{} <span class="badge-admin" title="Administrador">✔</span>', user.username)
    return format_html("{}", user.username)
