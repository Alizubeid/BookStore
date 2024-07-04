from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Auther,Customer
from .forms import AutherCreationForm,AutherChangeForm,CustomerChangeForm,CustomerCreationForm


class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ("username", "is_customer", "is_active",)
    list_filter = ("username", "is_customer", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Customer, CustomerAdmin)

class AutherAdmin(UserAdmin):
    add_form = AutherCreationForm
    form = AutherChangeForm
    model = Auther
    list_display = ("username", "is_auther", "is_active",)
    list_filter = ("username", "is_auther", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.register(Auther, AutherAdmin)