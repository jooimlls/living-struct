# views.py
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Brochure
import os

def brochure_list(request):
    brochures = Brochure.objects.filter(is_active=True)
    return render(request, 'brochure.html', {'brochures': brochures})

def download_brochure(request, pk):
    brochure = get_object_or_404(Brochure, pk=pk, is_active=True)

    # Increment download count
    brochure.download_count += 1
    brochure.save(update_fields=['download_count'])

    try:
        file_handle = brochure.file.open('rb')
        response = FileResponse(file_handle)
        filename = os.path.basename(brochure.file.name)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    except FileNotFoundError:
        raise Http404("File not found")
# Create your views here.


 