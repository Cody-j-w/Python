from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnections import connectToMySQL
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'canyoukeepit?'
mysql = connectToMySQL('advlogin')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'userlevel' in session:
        print(session['userlevel'])
    return render_template("index.html")

@app.route('/create_user', methods=['post'])
def register():
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    user = mysql.query_db("SELECT * FROM users")
    if len(request.form['first_name'])<1:
        flash('first name is a required field!','login')
    elif len(request.form['first_name'])>64:
        flash('first name must be under 64 characters!','login')
    else:
        if request.form['first_name'].isalpha() == True:
            session['first_name'] = request.form['first_name']
        else:
            flash('first name cannot contain numbers or special characters.','login')

    if len(request.form['last_name'])<1:
        flash('last name is a required field!','login')
    elif len(request.form['last_name'])>64:
        flash('last name must be under 64 characters!','login')
    else:
        if request.form['last_name'].isalpha() == True:
            session['last_name'] = request.form['last_name']
        else:
            flash('last name cannot contain numbers or special characters.','login')
    
    if len(request.form['password'])<8:
        flash('password must contain at least 8 characters.','login')
    elif len(request.form['password'])>64:
        flash('password must be under 64 characters in length.','login')
    else:
        if request.form['password'].isupper() == False and request.form['password'].islower() == False and request.form['password'].isalpha() == False and request.form['password'].isdigit() == False and request.form['password'].isalnum() == True:
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            print(pw_hash)
        else:
            flash('Password must contain at least one numeric character and one upper case character!','login')

    
    if request.form['password_confirm'] != request.form['password']:
        flash('passwords must match!','login')
    else:
        session['password_confirm'] = request.form['password_confirm']

    if len(request.form['email']) < 1:
        flash("E-mail cannot be blank.",'login')
    elif len(request.form['email'])>120:
        flash("E-mail must be below 120 characters.",'login')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid E-mail address.",'login')
    else:
        validateemails = mysql.query_db("SELECT email FROM users")
        print(type(validateemails))
        for x in validateemails:
            print(x)
            if x['email'] == request.form['email']:
                flash("that email is already taken!",'login')


    if '_flashes' in session.keys():
        return redirect('/')
    else:
        query = "INSERT INTO users (first_name, last_name, password_hash, email, created_at, updated_at, user_level) VALUES ( %(first_name)s, %(last_name)s, %(password_hash)s, %(email)s, NOW(), NOW(), 1);"
        data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'password_hash': pw_hash, 'email': request.form['email'], 'user_level': 1}
        mysql.query_db(query, data)

        return redirect('/success')

@app.route('/login', methods=['post'])
def login():
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password_hash'], request.form['password']):
            session['userid'] = result[0]['id']
            session['userlevel'] = result[0]['user_level']
            if result[0]['user_level'] == 9:
                return redirect('/admin_success')
            else:    
                return redirect('/success')
    flash('login failed', 'error')
    return redirect('/')

@app.route('/admin_success')
def admin_success():
    if session['userlevel'] == 1:
        flash("you're not allowed in there!")
        return redirect('/') 
    else:     
        return render_template('admin.html')

@app.route('/success')
def success():
    
    email = session['email']
    first_name = session['first_name']
    last_name = session['last_name']
    if 'userlevel' in session:
        print(session['userlevel'])
    if 'userid' in session:
        print(session['userid'])
    return render_template("user.html", email = email, first_name = first_name, last_name = last_name)



app.run(debug=True)