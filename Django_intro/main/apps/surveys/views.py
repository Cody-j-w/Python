from django.shortcuts import render, redirect, HttpResponse

def surveys(request):
    response = 'placeholder to display surveys'
    return HttpResponse(response)

def new(request):
    response = 'placeholder for page allowing creation of new surveys'
    return HttpResponse(response)