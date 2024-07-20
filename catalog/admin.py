from django.contrib import admin
from .models import Category, Product, Contacts, Version

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """Класс для регистрации версии в админке."""

    list_display = ("id", "product", "name", "number", "is_current")
    list_filter = ("product",)
    search_fields = ("name",)


admin.site.register(Contacts)
