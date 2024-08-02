from typing import Any
from django.core.management.base import BaseCommand


from users.models import User


class Command(BaseCommand):
    """Command that creates a new superuser"""

    def handle(self, *args: Any, **options: Any) -> str | None:
        users = User.objects.create(email="ivc@yandex.ru")
        users.set_password("123qwe")
        users.is_staff = True
        users.is_active = True
        users.is_superuser = True
        users.save()
