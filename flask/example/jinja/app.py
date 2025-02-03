from flask import Flask, render_template
import requests
import pandas as pd

app = Flask(__name__)

@app.route("/variable/<firstname>/<lastname>/")
def var(firstname: str, lastname: str):
  peson: dict[str, str] = {
    "firstname": firstname,
    "lastname": lastname,
  }
  return render_template("variable.html", person=peson)

@app.route("/get_btc/<int:value>")
def get_btc(value: int) -> str:
  response = requests.get(f"https://blockchain.info/tobtc?currency=USD&value={value}")
  return render_template("bitcoin_value.html", btc_value=response.text)

@app.route("/for")
def f():
  fruits: list[str] = [
    "apple",
    "banana",
    "cherry",
    "elderberry", 
    "watermelon",
    "grape",
    "kiwi",
    "lemon",
    "lime",
    "orange",
    "pear",
    "plum",
    "strawberry",
    "raspberry",
    "blueberry",
    "blackberry",
  ]

  return render_template("for.html", fruits=fruits)

@app.route("/if/<int:age>")
def i(age: int) -> str:
  return render_template("if.html", age=age)

@app.route("/safe")
def jinja_safe():
  html: str = '<script>alert("Hacked!!!")</script>'
  return render_template("safe.html", html=html)

@app.route("/")
def index() -> str:
  return render_template('index.html')

@app.route("/bootstrap")
def bootstrap_example():
  fruits: list[str] = [
    "apple",
    "banana",
    "cherry",
    "elderberry", 
    "watermelon",
    "grape",
    "kiwi",
    "lemon",
    "lime",
    "orange",
    "pear",
    "plum",
    "strawberry",
    "raspberry",
    "blueberry",
    "blackberry",
  ]
  veggies: list[str] = [
    "asparagus",
    "broccoli",
    "carrot",
    "daikon",
    "eggplant",
    "fennel",
    "garlic",
    "horseradish",
    "iceberg",
    "jicama",
    "kale",
    "leek",
    "mushroom",
    "onion",
    "parsnip",
    "quince",
  ]
  html = pd.DataFrame({
    "fruits": fruits,
    "veggies": veggies,
  }).to_html(classes="table table-striped table-bordered table-hover")
  return render_template("bootstrap.html", fruits=fruits, html=html)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)