from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
def home(request):
    return render(request,"living.html")
def enquire(request):
    return render(request,"enquire.html")
def project(request):
    return render(request,"project.html")
def about(request):
    return render(request,"about.html")
def brochure(request):
    return render(request,"brochure.html")
def cards(request):
    return render(request,"cards.html")

# from accounts.views import handle_lead_submission

# def home(request):
#     return handle_lead_submission(
#         request,
#         template_name="living.html",
#         redirect_name="Home"
#     )
