from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

def index(request):
    response = "placeholder to later display list of blogs"
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display form for creating a new blog'
    return HttpResponse(response)

def create(request):
    return HttpResponseRedirect('/')

def show(request, number):
    response = 'placeholder to display blog ' + number
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog ' + number
    return HttpResponse(response)

def destroy(request, number):
    return HttpResponseRedirect('/')

