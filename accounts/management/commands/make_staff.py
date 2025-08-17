from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Marca a un usuario como staff. Uso: python manage.py make_staff <username>"

def add_arguments(self, parser):
    parser.add_argument('username', type=str)

def handle(self, *args, **opts):
    U = get_user_model()
    try:
        u = U.objects.get(username=opts['username'])
    except U.DoesNotExist:
        raise CommandError("Usuario no encontrado")
    u.is_staff = True
    u.save()
    self.stdout.write(self.style.SUCCESS(f"{u.username} ahora es staff."))
