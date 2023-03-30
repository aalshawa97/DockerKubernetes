from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

def welcome(request):
    return HttpResponse('Welcome')

def goodbye(request):
    name = request.GET.get('name')
    if not name:
        return HttpResponse('Please provide a name!')
    return HttpResponse(f'Goodbye, {name}!')    