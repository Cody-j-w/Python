from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def dictionarySort():
    first_list = []
    last_list = []
    users = (
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'})

    for x in range(0,(len(users))):
        first_list.append(users[x]['first_name'])
        last_list.append(users[x]['last_name'])
    return render_template("index.html", first_name = first_list, last_name = last_list)

if __name__=="__main__":
    app.run(debug=True)