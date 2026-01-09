# admin.py
from django.contrib import admin
from .models import Brochure

@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at', 'download_count', 'is_active']
    list_filter = ['is_active', 'uploaded_at']
    search_fields = ['title', 'description']
    readonly_fields = ['download_count', 'uploaded_at']
# Register your models here.
