from django.urls import path
from . import views

app_name = "Enquire_About"

urlpatterns = [
    path("enquire/", views.enquire, name="Enquire"),
    path("about/", views.about, name="About"),
]
