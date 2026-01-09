# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.property_list, name='property_list'),
    path('cards/load-more/', views.load_more_properties, name='load_more_properties'),
    path('project/<slug:slug>/', views.property_detail, name='property_detail'),
]

