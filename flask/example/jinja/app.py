from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
  name = "Antonio"
  d = {
    "name": "antonio",
    "lastname": "pisanello"
  }
  return render_template("variable.html", name=name, dict_name=d)

@app.route("/index2")
def index2():
  name = "Antonio"
  d = {
    "name": "Miranda",
    "lastname": "tato"
  }
  return render_template("variable.html", name=name, dict_name=d)

@app.route("/for")
def jinja_for():
  fruits = [
    "apple",
    "banana",
    "orange",
    "watermelon",
    "peach",
    "strawberry"
  ]

  return render_template("for.html", fruits=fruits)

@app.route("/if")
def jinja_if():
  age = 2
  return render_template("if.html", age=age)

@app.route("/if/<int:age>")
def jinja_if_dynamic(age):
  return render_template("if.html", age=age)

@app.route("/table")
def jinja_table():
  json_obj = None
  with open("./data/posts.json", "r") as json_posts:
    json_obj = json.loads(json_posts.read())
  
  headers = list(json_obj[0].keys())
  return render_template("artem_example/table.html", headers=headers, posts=json_obj)

@app.route("/safe")
def jinja_safe():
  html = '<script>alert("Hacked!!!")</script>'
  return render_template("safe.html", html=html)


if __name__ == "__main__":
  app.run(debug=True)