from django.shortcuts import render

# Create your views here.
def portfolio_view(request):
    return render(request, 'projects/projects.html')
def about_me_view(request):
    return render(request, 'projects/about_me.html')
def experience_view(request):
    return render(request, 'projects/experience.html')
def projects_view(request):
    return render(request, 'portflio/project.html')