from django.contrib import admin
from .models import Section, Card

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'description', 'created_at', 'updated_at')
    list_filter = ('section',)
    search_fields = ('title', 'description')
    raw_id_fields = ('section',)
    readonly_fields = ('created_at', 'updated_at')