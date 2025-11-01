from django.shortcuts import render




# Create your views here.
def about_me_view(request):
    return render(request, 'portfolio/about_me.html')
def experience_view(request):
    return render(request, 'portfolio/experience.html')
def project_view(request):
    return render(request, 'porfolio/project.html')