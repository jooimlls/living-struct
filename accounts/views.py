from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.models import Lead
from .forms import LeadForm


def request_call(request):
    success = False
    error = None

    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']

            # 🔴 Check duplicate entry
            if Lead.objects.filter(email=email, mobile=mobile).exists():
                error = "You have already submitted this form."
            else:
                form.save()
                success = True
                form = LeadForm()  # clear form after success
                return redirect('Home')   # use your home url name
    else:
        form = LeadForm()

    return render(request, "header.html", {
        "form": form,
        "success": success,
        "error": error
    })