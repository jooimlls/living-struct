
from django.shortcuts import render
from .models import top_section, IntroSection, Benefit, Step, ContactInfo
from .models import WhoWeAre, AboutBlock, TeamMember
def enquire(request):
    hero = top_section.objects.first()
    print("HERO OBJECT:", hero)

    context = {
        'hero': hero,
        'intro': IntroSection.objects.first(),
        'benefits': Benefit.objects.all(),
        'steps': Step.objects.all(),
        'contact': ContactInfo.objects.first(),
    }
    return render(request, 'Enquire.html', context)


# def enquire(request):
#     context = {
#         'top_section': top_section.objects.first(),
#         'intro': IntroSection.objects.first(),
#         'benefits': Benefit.objects.all(),
#         'steps': Step.objects.all(),
#         'contact': ContactInfo.objects.first(),
#     }
#     return render(request, 'Enquire.html', context)


def about(request):
    context = {
        "who": WhoWeAre.objects.first(),
        "about_blocks": AboutBlock.objects.all(),
        "team": TeamMember.objects.all(),
    }
    return render(request, "about.html", context)


# Create your views here.
