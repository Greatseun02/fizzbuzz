from flask import Flask, render_template

app = Flask(__name__)

rangeOfNumbers = range(1, 100)

@app.route("/")
def index():
    return '''<a href="/fizzbuzz">Link to fizzbuzz</a>'''

@app.route("/fizzbuzz")
def fizzbuzz():
    return render_template("index.html", rangeOfNumbers = rangeOfNumbers)