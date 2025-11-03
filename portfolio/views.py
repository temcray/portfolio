from django.shortcuts import render
from .models import Experience




# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about_me.html')
def experience_view(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {'experiences': experiences})
