from django.urls import path, include
from project import views 


urlpatterns = [

path('', include('portfolio.urls')),
path('project/', views.portfolio_view, name= 'project'),
]