from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from apps.auths.models import Profile, Otp

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id", "get_phone", "get_email", "get_role")
    inlines = (UserProfileInline,)
    ordering = ("-id",)

    fieldsets = (
        ("System  Data", {"fields": ("username", "password")}),
        (
            "Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {"classes": ("collapse",), "fields": ("last_login", "date_joined")},
        ),
    )

    def get_phone(self, obj):
        if phone := obj.profile.phone_number:
            return str(phone)
        return None

    get_phone.short_description = "Phone Number"

    def get_email(self, obj):
        if email := obj.profile.email:
            return str(email)
        return None

    get_email.short_description = "Email"

    def get_role(self, obj):
        if role := obj.profile.role:
            return str(role)
        return None

    get_role.short_description = "Role"


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = ("id", "email", "phone_number", "created_at")
