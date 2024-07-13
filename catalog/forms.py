from django import forms

from .models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "imagePreview", "category", "price")
