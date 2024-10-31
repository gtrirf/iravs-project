from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import About


@admin.register(About)
class AboutAdmin(ModelAdmin):
    unfold_collapse = True
    list_display = ('title', 'order', 'created_at', 'updated_at')

    fieldsets = (
        ('Main Title and Order', {
            'fields': ('title', 'order'),
            'classes': ('collapse',),
        }),
        ('Titles by Language', {
            'fields': ('title_uz', 'title_ru'),
            'classes': ('collapse',),
        }),
        ('Body Content', {
            'fields': ('body',),
            'classes': ('collapse',),
        }),
        ('Body Content by Language', {
            'fields': ('body_uz', 'body_ru'),
            'classes': ('collapse',),
        }),
        ('Images', {
            'fields': ('image', 'about_image'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
