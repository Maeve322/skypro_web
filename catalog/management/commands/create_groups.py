# catalog/management/commands/create_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = "Create moderator group with specific permissions"

    def handle(self, *args, **kwargs):
        # Создаем группу модераторов
        moderator_group, created = Group.objects.get_or_create(name="Moderator")

        # Определяем тип контента для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Определяем и создаем необходимые права, если они не существуют
        permissions = [
            Permission.objects.get_or_create(
                codename="can_unpublish_product",
                name="Can unpublish product",
                content_type=content_type,
            )[0],
            Permission.objects.get_or_create(
                codename="change_description_product",
                name="Can change product description",
                content_type=content_type,
            )[0],
            Permission.objects.get_or_create(
                codename="change_category_product",
                name="Can change product category",
                content_type=content_type,
            )[0],
        ]

        # Назначаем права группе
        for permission in permissions:
            moderator_group.permissions.add(permission)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully created Moderator group with specific permissions"
            )
        )
