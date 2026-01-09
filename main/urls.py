from django.urls import path
from .views import Main_living

urlpatterns = [
    path('', Main_living, name='Home'),
]
