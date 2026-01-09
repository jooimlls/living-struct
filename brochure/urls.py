# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('brochures/', views.brochure_list, name='brochure_list'),
    path('brochures/download/<int:pk>/', views.download_brochure, name='download_brochure'),
]