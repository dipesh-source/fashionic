"""Admin.py for reguster model."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""

    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone",
                    "address",
                    "start_date",
                    "end_date",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_editable = ["username", "phone"]
    list_display = (
        "id",
        "email",
        "username",
        "phone",
        "start_date",
        "end_date",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("email", "first_name", "last_name", "phone", "username")
    ordering = ("email", "username")


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)


# @admin.register(OutstandingToken)
# class OutstandingTokenAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "jit", "token", "created_at", "expires_at"]


# @admin.register(BlacklistedToken)
# class BlacklistedTokenAdmin(admin.ModelAdmin):
#     list_display = ["id", "token", "blacklisted_at"]
