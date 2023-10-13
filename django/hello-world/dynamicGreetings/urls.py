from . import views
from django.urls import path

# Kinda namespace of multiapp projects 
app_name = 'dynamicGreetings'
urlpatterns = [
    path('', views.index, name='index'),
    path('listSports', views.listSports, name='listSports'),
    path('editSport', views.editSport, name='editSport'),
    path('saveSport', views.saveSport, name='saveSport'),
    path('listCountries', views.listCountries, name='listCountries'),
    path('editCountry', views.editCountry, name='editCountry'),
    path('saveCountry', views.saveCountry, name='saveCountry'),
    path('listPersons', views.listPersons, name='listPersons'),
    path('editPerson', views.editPerson, name='editPerson'),
    path('savePerson', views.savePerson, name='savePerson')           
]
