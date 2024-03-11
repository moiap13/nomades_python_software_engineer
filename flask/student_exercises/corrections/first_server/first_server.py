from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
  json_obj = None
  print(type(json_obj))
  with open("./posts.json", "r") as json_posts:
    json_obj = json.loads(json_posts.read())
  
  print(type(json_obj))
  print((json_obj[0]['userId']))
  return "<h1>Hello from flask | welcome to the flask class</h1>"

@app.route("/hello/how/<name>")
def test_name(name):
  return f"Hello {name}"

@app.route("/age/<int:age>")
def test_age(age):
  if age < 18:
    return "Minor"
  return "Major"

if __name__ == "__main__":
  app.run(debug=True)