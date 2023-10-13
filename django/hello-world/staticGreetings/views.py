from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

def index(request):
    template = loader.get_template('staticGreetings/index.html')
    context = {}
    return HttpResponse(template.render(context, request))    

def oldFashionedLink(request):
    template = loader.get_template('staticGreetings/oldFashionedLink.html')
    context = {}
    return HttpResponse(template.render(context, request))    

def greetByName(request):
    template = loader.get_template('staticGreetings/greetByName.html')
    print('Form name: ' + str(request.POST.get('name')))
    context = {
        'name': request.POST.get('name')
    }
    return HttpResponse(template.render(context, request))    

def dynamicLink(request, name):
    template = loader.get_template('staticGreetings/greetByNameGET.html')
    context = {
        'name': name
    }
    return HttpResponse(template.render(context, request))       
