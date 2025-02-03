from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() -> str:
 return "<h1>Hello PPL !</h1><img src='https://en.wikipedia.org/static/images/icons/wikipedia.png'>"

@app.route("/hello/<name>/<name2>")
def hello_name(name: str, name2: str) -> str:
  print(type(name))
  return f"<h1>Hello <span style='color: red'>{name}</span></h1><h2>{name2}</h2>"

@app.route("/hello/<name>/<int:age>")
def hello_age(name: str, age: int) -> str:
  return f"<h1>Hello <span style='color: red'>{name}</span></h1><p>You are {age} years old</p>"

@app.route('/allow/<int:age>')
def allow_voting(age):
    return "You are allowed to enter the voting website" if age >= 18 else "You are not allowed to enter the voting website"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)