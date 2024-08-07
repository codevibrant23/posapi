from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add fields to display in the admin list view
    list_display = ('username', 'email', 'company_name', 'number_of_outlets', 'number_of_employees', 'phone_number', 'is_staff', 'is_active')
    # Add fields to the admin form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'company_name', 'number_of_outlets', 'number_of_employees', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'company_name', 'number_of_outlets', 'number_of_employees', 'phone_number'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)