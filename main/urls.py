from main import views
from django.urls import path

urlpatterns = [
   path('projects/',views.projects,name='projects'),
   path('Accomplishments/',views.Accomplishments,name='Accomplishments'),
   path('',views.index,name='index')
]