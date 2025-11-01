from django.shortcuts import render

#create your views here
def about_me_view(request):
    return render(request, 'portfolio/about_me.html')