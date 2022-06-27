from django.shortcuts import render
from django.http import HttpResponse


def home(request,name):
    message = 'Salut tout le monde '+name
    return HttpResponse(message)
