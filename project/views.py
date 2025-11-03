from django.shortcuts import render
from . import models
# Create your views here.
def portfolio_view(request):
    projects_list = models.Project.objects.all()
    context = {'projects': projects_list}
    return render(request, 'projects/project.html', context)
