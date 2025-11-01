from django.urls import path
from project import views 


urlpatterns = [
path('project/', views.portfolio_view, name= 'project'),
]