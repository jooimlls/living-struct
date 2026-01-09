# views.py
# cards/views.py
from django.shortcuts import render, get_object_or_404
from .models import Property
from django.http import JsonResponse

def property_list(request):
    status = request.GET.get('status', 'completed')

    if status == 'ongoing':
        properties = Property.objects.filter(is_active=True)[:6]

    elif status == 'upcoming':
        # No DB change → upcoming has no records yet
        properties = Property.objects.none()

    else:  # completed (default)
        properties = Property.objects.filter(is_active=False)[:6]
    
    return render(request, 'cards.html', {
        'properties': properties,
        'status': status
    })

def load_more_properties(request):
    offset = int(request.GET.get('offset', 0))
    status = request.GET.get('status', 'completed')

    if status == 'ongoing':
        qs = Property.objects.filter(is_active=False)

    elif status == 'upcoming':
        qs = Property.objects.none()

    else:  # completed
        qs = Property.objects.filter(is_active=True)
    qs = qs[offset:offset + 6]  # ✅ FIXED

    data = []
    for p in qs:
        data.append({
            'title': p.title,
            'short_description': p.short_description,
            'image': p.main_card_image.url if p.main_card_image else '',
            'slug': p.slug
        })

    return JsonResponse({'properties': data})

def property_detail(request, slug):
    property = get_object_or_404(Property, slug=slug, is_active=True)
    return render(request, 'project.html', {
        'property': property
    })



# Create your views here.
