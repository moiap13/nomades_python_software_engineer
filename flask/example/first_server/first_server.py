from flask import Flask, render_template, request, session, redirect, url_for
import csv
from functools import wraps

app = Flask(__name__)
app.secret_key = "supersecret"

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("logged" in session and session["logged"]): # -> je ne suis pas loggé
      return redirect(url_for('login'))
    
    return func(*args, **kwargs)
  return inner

@app.route("/")
def index():
  return render_template("index.html", name="John")

@app.route("/fruits")
def fruits():
  fruits = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange", "pear", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
  return render_template("publics/fruits.html", fruits=fruits, flag=False)

@app.route("/hello/<user>")
def index_dyn(user):
  print(type(user))
  return render_template("publics/index.html", name=user)

@app.route("/secret")
@authenticated
def secret():
  return "Secret Page"

@app.route("/login", methods=["GET", "POST"])
def login():
  if "logged" in session and session["logged"]:
    return redirect(url_for('userinfo'))

  if request.method == "POST":
    email: str = request.form.get("tbx_email")
    pwd: str = request.form.get("tbx_password")

    with open('users.csv') as users_csv_file:
      rows = csv.reader(users_csv_file)
      rows = csv.DictReader(users_csv_file)
      # next(rows)
      for row in rows:
        print(row)
        if row["email"] == email and row["password"] == pwd:
          session["logged"] = True
          session["user_email"] = email
          session["user_password"] = pwd
          session["user_id"] = row["uid"]
          return redirect(url_for('userinfo'))

  return render_template("login/login.html")

@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('login'))

@app.route("/user/info")
@authenticated
def userinfo():
  return """
    <ul>
    <li>{}</li>
    <li>{}</li>
    <li>{}</li>
    </ul>
  """.format(session["user_email"], session["user_password"], session["user_id"])
  
 

if __name__ == "__main__":
  app.run(port=8080, host='0.0.0.0', debug=True)