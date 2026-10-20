
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Cria o administrador inicial, caso não exista."

    def handle(self, *args, **options):
        username = os.getenv("ADMIN_USERNAME")
        password = os.getenv("ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError(
                "Configure ADMIN_USERNAME e ADMIN_PASSWORD."
            )

        User = get_user_model()

        if User.objects.filter(username=username).exists():
            self.stdout.write("Usuário já existe. Nenhuma alteração.")
            return

        User.objects.create_superuser(
            username=username,
            email="",
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Administrador criado com sucesso.")
        )
