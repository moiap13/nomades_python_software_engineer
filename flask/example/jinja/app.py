from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/variable/<firstname>/<lastname>/<color>")
def var(firstname, lastname, color):
  return render_template("variable.html", 
                         name=firstname, 
                         lastname=lastname, 
                         color=color
  )

@app.route("/for")
def for_loop():
  names: list[str] = [
    "cyrille",
    "marcus",
    "mostepha",
    "sami",
    "cyril",
    "miguel",
    "stéphane",
    "naomi"
  ]
  return render_template("for_block.html", names=names)

@app.route("/if/<int:age>")
def i(age: int) -> str:
  return render_template("if.html", age=age)

@app.route("/filter")
def filter_route():
  names: list[str] = [
    "cyrille",
    "marcus",
    "mostepha",
    "sami",
    "cyril",
    "miguel",
    "stéphane",
    "naomi"
  ]
  return render_template("filter.html", names=names)

@app.route("/safe")
def safe():
  html = "ceci est un commentaire <script>alert('Hacked !!!')</script>"
  return render_template("safe.html", html=html)

@app.route("/pandas")
def pan():
  fruits: list[str] = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew"
  ]

  vegetables: list[str] = [
    "asparagus",
    "broccoli",
    "carrot",
    "daikon",
    "eggplant",
    "fennel",
    "garlic",
    "horseradish"
  ]

  df = pd.DataFrame({
    "fruits": fruits,
    "vegetables": vegetables
  })

  return render_template("pandas.html", df=df.to_html(classes="table table-striped table-hover"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8081, debug=True)