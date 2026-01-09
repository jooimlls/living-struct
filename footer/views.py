from django.shortcuts import render
from .models import Footer

def footer_context(request):
    footer = Footer.objects.filter(is_active=True).first()
    return {
        'footer': footer
    }

# Create your views here.
