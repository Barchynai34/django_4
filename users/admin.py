from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import GeekUserCreationForm, GeekUserChangeForm
from users.models import GeekUser


# Register your models here.	
class GeekUserAdmin(UserAdmin):
    add_form = GeekUserCreationForm
    form = GeekUserChangeForm
    model = GeekUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Основная информация", {"fields": ("email", "password")}),
        ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Даты", {"fields": ("date_joined", "last_login")}),
    )
    add_fieldsets = (
        ("Создать пользователя", {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions",
            )
        }),
    )


admin.site.register(GeekUser, GeekUserAdmin)


