from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        'date':strftime('%Y/%m/%d', gmtime()),
        'time':strftime('%H:%M %p', gmtime())
    }

    return render(request, 'timepiece/index.html', context)