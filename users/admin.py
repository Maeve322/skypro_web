from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from .forms import UserRegistrationForm, UserProfileForm


class UserAdmin(BaseUserAdmin):
    add_form = UserRegistrationForm
    form = UserProfileForm
    list_display = (
        "email",
        "first_name",
        "last_name",
        "avatar_tag",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("password",)}),
        (
            "Personal info",
            {
                "fields": (
                    "email",
                    "avatar",
                    "phone",
                    "country",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "nickname", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email", "nickname", "first_name", "last_name")
    ordering = ("email",)
    readonly_fields = ("avatar_tag",)

    def avatar_tag(self, obj):
        if obj.avatar:
            return mark_safe(
                f"""
                  <div style="position: relative; padding-top: 80px;">
                      <img src="{obj.avatar.url}" style="
                          width: 100px;
                          height: 100px;
                          border-radius: 10%;
                          object-fit: cover;
                          position: absolute;
                          top: -10px;
                          left: 0px;
                      " />
                  </div>
              """
            )
        return "-"

    avatar_tag.short_description = "Avatar"


admin.site.register(User, UserAdmin)
