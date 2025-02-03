from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() -> str:
  return render_template('index.html')

@app.route("/hello/<name>")
def hello(name: str) -> str:
  print(type(name))
  return f"<h1>Hello <span style='color: red'>{name}</span></h1>"

@app.route("/allow/<int:age>")
def age(age: int) -> str:
  return "You are allowed to vote using this website" if age >= 18 else "You are not able to vote using this website"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)