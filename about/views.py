from django.shortcuts import render
from .models import About

def about_rs(request):
    """
    Renders the most recent information on the about page
    for the website :model:`about.About`.
    """
    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {"about": about},
    )