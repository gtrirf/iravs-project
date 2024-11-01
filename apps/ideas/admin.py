from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Ideas, ReplyToIdea, IdeasImages


class IdeasImagesInline(admin.TabularInline):
    model = IdeasImages
    extra = 1
    fields = ('image',)
    max_num = 5


@admin.register(Ideas)
class IdeasAdmin(ModelAdmin):
    unfold_collapse = True
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    fields = ('name', 'email', 'body', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ReplyToIdea)
class ReplyToIdeaAdmin(ModelAdmin):
    unfold_collapse = True
    list_display = ('__str__','created_at', 'updated_at')
    search_fields = ('idea__name',)
    fields = ('idea', 'body', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [IdeasImagesInline]
