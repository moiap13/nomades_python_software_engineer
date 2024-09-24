from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/variable")
def variable():

  d = {
    "n": "",
    "l": ""
  }

  d["n"] = "Antonio"
  return render_template("variable.html", d=d)

@app.route("/for")
def jinja_for():
  fruits = [
    "apple",
    "banana",
    "orange",
    "watermelon",
    "peach",
    "strawberry",
    "pear"
  ]

  return render_template("for.html", fruits=fruits)

@app.route("/if")
def jinja_if():
  age = 2
  return render_template("if.html", age=age)

@app.route("/filter")
def jinja_filter():
  name = "antonio"
  return render_template("filter.html", name=name)

@app.route("/safe")
def jinja_safe():
  html = '<script>alert("Hacked!!!")</script>'
  return render_template("safe.html", html=html)

if __name__ == "__main__":
  app.run(debug=True)