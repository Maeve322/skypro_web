import random
import string
import secrets

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, RedirectView
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from config.settings import EMAIL_HOST_USER

# Create your views here.

from users.models import User
from users.forms import UserRegistrationForm, UserProfileForm, PasswordResetForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейти по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserLoginView(LoginView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = User.objects.get(email=email)
                new_password = generate_password()
                user.password = make_password(new_password)
                user.save()
                try:
                    send_mail(
                        "Восстановление пароля",
                        f"Ваш новый пароль: {new_password}",
                        EMAIL_HOST_USER,
                        [user.email],
                        fail_silently=False,
                    )
                    messages.success(
                        request,
                        f"Новый пароль отправлен на почтовый ящик {EMAIL_HOST_USER}",
                    )
                except Exception:
                    messages.error(
                        request,
                        "Ошибка при отправке письма. Попробуйте еще раз.",
                    )
                return redirect("users:login")
            except User.DoesNotExist:
                messages.error(
                    request,
                    f"Пользователь с почтой {EMAIL_HOST_USER} не существует",
                )
    else:
        form = PasswordResetForm()
    return render(request, "users/password_reset.html", {"form": form})


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:login")

    template_name = "users/profile.html"

    def get_object(self, queryset: QuerySet[any] | None = ...) -> Model:
        return self.request.user


class CustomLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy("users:login")

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import logout

        logout(request)
        return super().get(request, *args, **kwargs)
