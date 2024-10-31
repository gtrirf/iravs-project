from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin, GroupAdmin as DefaultGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin

# Avval User va Group modellarini ro'yxatdan chiqarish
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(DefaultUserAdmin, ModelAdmin):
    unfold_collapse = True  # Barcha bo'limlar katlanadigan qilib qo'yiladi
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    fieldsets = (
        ('Main Information', {
            'fields': ('username', 'password'),
            'classes': ('collapse',),
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email'),
            'classes': ('collapse',),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', 'collapse'),  # Keng va katlanadigan bo'lim
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name'),
        }),
    )


@admin.register(Group)
class CustomGroupAdmin(DefaultGroupAdmin, ModelAdmin):
    unfold_collapse = True
    list_display = ('name',)

    fieldsets = (
        ('Group Information', {
            'fields': ('name', 'permissions'),
            'classes': ('collapse',),
        }),
    )
