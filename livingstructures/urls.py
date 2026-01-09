"""
URL configuration for livingstructures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from livingstructures import views
from cards.views import property_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('enquire/', views.enquire, name='Enquire'),
    path('project/', views.project, name='Project'),
    # path('about/', views.about, name='About'),
    path('brochure/brochure', views.brochure, name='Brochure'),
    path('living/cards/', property_list, name='Cards'),
    path('', include('accounts.urls')), 
    path('living/', include('cards.urls')),
    path('living/', include('brochure.urls')),
    path('', include('main.urls')),
    path('', include('Enquire_About.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



