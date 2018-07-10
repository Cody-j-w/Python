from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<size>/<color>')
def playground(size, color):
    x=int(size)
    return render_template("index.html", length=x, blockcolor=color)
if __name__=="__main__":
    app.run(debug=True)