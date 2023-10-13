from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import Country, Person, Sport

def index(request):
    template = loader.get_template('dynamicGreetings/index.html')
    context = {}
    return HttpResponse(template.render(context, request))   

def listSports(request):
    sports = Sport.objects.all()
    return render(request, 'dynamicGreetings/listSports.html', {'sports': sports})

def saveSport(request):
    sportName = request.POST.get('nameName')
    sportId = request.POST.get('nameHiddenId')
    if sportId == None:
        print('New sport name: ', sportName)
        newSport = Sport(name = sportName)
        newSport.save()
        print(newSport)
    else:
        sport = Sport.objects.get(pk=sportId)
        sport.name = sportName
        sport.save()
    return listSports(request)
    
def editSport(request):
    sportId = request.POST.get('nameHiddenId')
    sport = None
    if sportId != None:
        print('Sport id. to edit: ', str(sportId))
        sport = Sport.objects.get(pk=sportId)
        print('Sport to edit id: ', str(sport.id), ', name: ', sport.name)
    return render(request, 'dynamicGreetings/editSport.html', {'sport': sport})
    
def listCountries(request):
    countrys = Country.objects.all()
    return render(request, 'dynamicGreetings/listCountries.html', {'countries': countrys})

def saveCountry(request):
    countryName = request.POST.get('nameName')
    countryId = request.POST.get('nameHiddenId')
    if countryId == None:
        print('New country name: ', countryName)
        newCountry = Country(name = countryName)
        newCountry.save()
        print(newCountry)
    else:
        country = Country.objects.get(pk=countryId)
        country.name = countryName
        country.save()
    return listCountries(request)
    
def editCountry(request):
    countryId = request.POST.get('nameHiddenId')
    country = None
    if countryId != None:
        print('Country id. to edit: ', str(countryId))
        country = Country.objects.get(pk=countryId)
        print('Country to edit id: ', str(country.id), ', name: ', country.name)
    return render(request, 'dynamicGreetings/editCountry.html', {'country': country})
    
def listPersons(request):
    persons = Person.objects.all()
    return render(request, 'dynamicGreetings/listPersons.html', {'persons': persons})    
    
def savePerson(request):
    personName = request.POST.get('nameName')
    countryId = request.POST.get('countryId')
    birthDate = request.POST.get('dateBirth')
    personId = request.POST.get('nameHiddenId')
    if personId == None:
        print('New person name: ', personName)
        print('New person country id: ', countryId)
        print('New person birth date: ', birthDate)
        country = Country.objects.get(pk=countryId)
        print('New person nationality: ', country.name)
        newPerson = Person(name = personName, nationalty=country, dateBirth=birthDate)
        newPerson.save()
        print(newPerson)
    else:
        person = Person.objects.get(pk=personId)
        person.name = personName
        person.save()
    return listPersons(request)
    
def editPerson(request):
    personId = request.POST.get('nameHiddenId')
    person = None
    if personId != None:
        print('Person id. to edit: ', str(personId))
        person = Person.objects.get(pk=personId)
        print('Person to edit id: ', str(person.id), ', name: ', person.name)
    return render(request, 'dynamicGreetings/editPerson.html', {'person': person})
    

