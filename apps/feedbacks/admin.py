from django.contrib import admin
from .models import Feedbacks
from django.utils.html import format_html
from unfold.admin import ModelAdmin


@admin.register(Feedbacks)
class FeedbacksAdmin(ModelAdmin):
    unfold_collapse = True
    list_display = ('body', 'fullname', 'email_or_number', 'read', 'created_at')
    search_fields = ('fullname', 'email_or_number')
    list_filter = ('read',)

    fieldsets = (
        ('Feedback Details', {
            'fields': ('body', 'fullname', 'email_or_number', 'read'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not obj.read:
            obj.read = True
        super().save_model(request, obj, form, change)
