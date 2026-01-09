from django.urls import path
from . import views

urlpatterns = [
    path('header', views.request_call, name='header'),
    # path('project/', views.request_onpro, name='project'),
    # path('about/', views.request_onabout, name='about'),
    # path('cards/', views.request_oncards, name='cards'),
    # path('enquire/', views.request_onenquier, name='enquire'),
]