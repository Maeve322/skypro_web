from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from users.models import User

from catalog.forms import StyleFormMixin


class UserRegistrationForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)


class UserProfileForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "phone",
            "avatar",
            "country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # to hide the password field in the profile form
        self.fields["password"].widget = forms.HiddenInput()
