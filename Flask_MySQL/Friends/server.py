from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
mysql = connectToMySQL('friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print("grabbing friends", friends)
    return render_template("index.html", friends = friends)

@app.route('/create_user', methods=['post'])
def register():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {'first_name': request.form['first_name'], 'last_name': request.form['last_name'], 'occupation': request.form['occupation']}
    
    mysql.query_db(query, data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
