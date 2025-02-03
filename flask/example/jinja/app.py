from flask import Flask, render_template

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

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8081, debug=True)