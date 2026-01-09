from django.shortcuts import render
from .models import MainModel, Carousel, CoreValue, MissionVision, Overview, Stat

def Main_living(request):
    context = {
        'main': MainModel.objects.filter(is_active=True).first(),
        'slides': Carousel.objects.filter(is_active=True),
        'core_values': CoreValue.objects.all(),
        'mv': MissionVision.objects.first(),
        'overview': Overview.objects.first(),
        'stats': Stat.objects.all(),
    }
    return render(request, 'living.html', context)

# Create your views here.
