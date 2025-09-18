from django.shortcuts import render
from .models import Teaser

def home(request):
    teasers = Teaser.objects.all()[:6]
    return render(request, 'home.html', {'teasers': teasers})

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')
