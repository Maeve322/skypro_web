from django.forms import ModelForm, BooleanField
from django.core.validators import ValidationError
from .models import Product, Version


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class CreateProduct(StyleFormMixin, ModelForm):
    """Класс для создание форм для модели Продукт"""

    banned_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ("name", "description", "imagePreview", "category", "price")

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        if cleaned_data.lower() in self.banned_words:
            raise ValidationError(
                "Извините, но в названии продукта нельзя использовать запрещенные слова."
            )

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        if cleaned_data.lower() in self.banned_words:
            raise ValidationError(
                "Извините, но в описании продукта нельзя использовать запрещенные слова."
            )

        return cleaned_data


class VersionForm(StyleFormMixin, ModelForm):

    class Meta:
        model = Version
        fields = ("id", "product", "name", "number", "is_current")
