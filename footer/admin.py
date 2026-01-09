
from django.contrib import admin
from .models import Footer

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('Footer_email', 'Footer_phone', 'is_active', 'created_at')
    list_filter = ('is_active',)

# Register your models here.
