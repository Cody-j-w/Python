from flask import Flask, render_template, request, redirect, session, flash
import re
import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="yourthoughtsmatter"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def surveyForm():

    if len(request.form['first_name'])<1:
        flash('first name is a required field!')
    elif len(request.form['first_name'])>64:
        flash('first name must be under 64 characters!')
    else:
        if request.form['first_name'].isalpha() == True:
            session['first_name'] = request.form['first_name']
        else:
            flash('first name cannot contain numbers or special characters.')

    if len(request.form['last_name'])<1:
        flash('last name is a required field!')
    elif len(request.form['last_name'])>64:
        flash('last name must be under 64 characters!')
    else:
        if request.form['last_name'].isalpha() == True:
            session['last_name'] = request.form['last_name']
        else:
            flash('last name cannot contain numbers or special characters.')

    if len(request.form['email'])<1:
        flash('E-mail is a required field!')
    elif len(request.form['email'])>120:
        flash('E-mail must be under 120 characters!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("please enter a valid E-mail address")
    else:
        session['email'] = request.form['email']

    if len(request.form['password'])<8:
        flash('password must contain at least 8 characters.')
    elif len(request.form['password'])>64:
        flash('password must be under 64 characters in length.')
    else:
        if request.form['password'].isupper() == False and request.form['password'].islower() == False and request.form['password'].isalpha() == False and request.form['password'].isdigit() == False:
            session['password'] = request.form['password']
        else:
            flash('Password must contain at least one numeric character and one upper case character!')
            return redirect('/')
    
    if request.form['password_confirm'] != request.form['password']:
        flash('passwords must match!')
    else:
        session['password_confirm'] = request.form['password_confirm']
    

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        flash('Thank you for the information!')
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)