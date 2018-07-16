from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.courselist.models import *

def index(request):

    return render(request, 'courselist/index.html', {'courses': Course.objects.all()})

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/courses/')
    else:
        course_description = Description.objects.create(contents = request.POST['course_description'])
        Course.objects.create(course_name = request.POST['course_name'], description = course_description)
        return redirect ('/courses/')

def course(request, id):
    return render(request, 'courselist/course.html', {'courses': Course.objects.get(id=id)})

def comment(request, id):
    this_course = Course.objects.get(id=id)
    new_comment = Comment.objects.create(comment = request.POST['comment'], course = this_course)
    return redirect('/courses/' +str(id))

def delete(request, id):
    return render(request, 'courselist/destroy.html', {'courses': Course.objects.get(id = id)})


def destroy(request, id):
    Course.objects.get(id = id).delete()
    return redirect('/courses')

