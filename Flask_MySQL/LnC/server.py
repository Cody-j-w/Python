from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app = Flask(__name__)
mysql = connectToMySQL('lead_gen_business')

@app.route('/')
def index():
    clients = mysql.query_db("SELECT clients.first_name, clients.last_name, COUNT(clients.client_id) as leads from clients JOIN sites on clients.client_id = sites.client_id JOIN leads on leads.site_id = sites.site_id GROUP BY clients.client_id")
    print("organizing data structure", clients)
    return render_template("LnCtest.html", clients = clients)

app.run(debug=True)