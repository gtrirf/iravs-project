from .models import MainPage, Socials
from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin


@admin.register(MainPage)
class MainPageAdmin(ModelAdmin):
    unfold_collapse = True  # Collapsible bo'lim
    unfold_collapse_list_display = ['full_name', 'job']  # Umumiy ma'lumotlarni asosiy sahifada ko'rsatish

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px; border-radius: 50%;" />',
            obj.image.url
        )
    image_tag.short_description = 'Image'

    list_display = ['full_name', 'job', 'created_at', 'updated_at', 'image_tag']
    fieldsets = (
        ('Main Information', {
            'fields': ('full_name', 'job', 'body', 'image'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Socials)
class SocialsAdmin(ModelAdmin):
    unfold_collapse = True
    list_display = ['social_name', 'social_url', 'created_at', 'updated_at']
    fieldsets = (
        ('Social Information', {
            'fields': ('social_name', 'social_url'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
