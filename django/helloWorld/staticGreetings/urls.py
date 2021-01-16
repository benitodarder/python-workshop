from . import views
from django.urls import path

# Kinda namespace of multiapp projects 
app_name = 'staticGreetings'
urlpatterns = [
    path('', views.index, name='index'),
    path('oldFashionedLink', views.oldFashionedLink, name='oldFashionedLink'),
    path('greetByName', views.greetByName, name='greetByName'),
    path('<str:name>/dynamicLink', views.dynamicLink, name='dynamicLink')
]
