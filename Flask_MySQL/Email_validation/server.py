from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = 'canyoukeepit?'
mysql = connectToMySQL('mydb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create_user', methods=['post'])
def register():
    emails = mysql.query_db("SELECT * FROM emails")
    if len(request.form['email']) < 1:
        flash("Please enter a valid E-mail address!")
        return redirect('/')
    elif len(request.form['email'])>120:
        flash("E-mail must be below 120 characters!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid E-mail address!")
        return redirect('/')
    else:
        validateemails = mysql.query_db("SELECT name FROM emails")
        print(type(validateemails))
        for x in validateemails:
            print(x)
            if x['name'] == request.form['email']:
                flash("that email is already taken!")
                return redirect('/')
            
        query = "INSERT INTO emails (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        data = {'name': request.form['email']}
        mysql.query_db(query, data)
        return redirect('/results')
        
@app.route('/results')
def show():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template("results.html", emails = emails)

if __name__ == "__main__":
    app.run(debug=True)

