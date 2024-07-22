from django.db import models

from users.models import User, NULLABLE


class Contacts(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    phone = models.CharField(max_length=100, verbose_name="Телефон")

    def __str__(self) -> str:
        return f"{self.name} {self.address} {self.phone}"

    class Meta:
        verbose_name = "ContactsView"
        verbose_name_plural = "ContactsViews"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(max_length=100, verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    imagePreview = models.ImageField(
        upload_to="products/preview/", blank=True, null=True
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категория"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        on_delete=models.CASCADE,
        related_name="products",
        **NULLABLE,
    )

    # manufactured_at = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.name} {self.description} {self.category} \
            {self.created_at}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Version(models.Model):
    """Модель для версии продукта"""

    product = models.ForeignKey(
        Product,
        related_name="versions",
        verbose_name="Продукт",
        on_delete=models.CASCADE,
    )
    number = models.PositiveIntegerField(
        verbose_name=" Номер версии", blank=True, null=True
    )
    name = models.CharField(max_length=150, verbose_name="Название версии")
    is_current = models.BooleanField(
        default=True, verbose_name="Признак актуальности"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ("name",)

    def __str__(self):
        return self.name
