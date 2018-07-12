from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'surveyform/index.html')

def process(request):
    if request.method == 'POST':
        error = 0
        if len(request.POST['name'])<1:
            flash('name is a required field!')
            error +=1
        elif len(request.POST['name'])>64:
            flash('Name must be under 64 characters!')
            error +=1
        else:
           request.session['name'] = request.POST['name']

        if len(request.POST['email'])<1:
            flash('E-mail is a required field!')
            error +=1
        elif len(request.POST['email'])>120:
            flash('E-mail must be under 120 characters!')
            error +=1
        else:
           request.session['email'] = request.POST['email']

        request.session['language'] = request.POST['language']

        if len(request.POST['comments'])<1:
            flash('Comments is a required field!')
            error +=1
        elif len(request.POST['comments'])>120:
            flash('Comments must be under 120 characters!')
            error +=1
        else:
           request.session['comments'] = request.POST['comments']

        request.session['location'] = request.POST['location']
        if error > 1:
            return redirect('/')
        else:
            return redirect('surveyform/results')

def results(request):
    return render(request, 'surveyform/results.html')