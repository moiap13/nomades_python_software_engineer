from flask import Flask, render_template, request, session, redirect, url_for
import os
import csv
import hashlib
from functools import wraps

CURR_URL = os.path.dirname(__file__)
app = Flask(__name__)
app.secret_key = "secret"

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("loggedin" in session and session["loggedin"]):
      return redirect(url_for('login'))
    
    assert session["loggedin"]
    return func(*args, **kwargs)
  return inner

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then open a csv file and add the new user
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of th e input
    password = request.form.get("tbxPwd")
    pwd_h = hashlib.sha256(password.encode()).hexdigest()
    uid = request.form.get("tbxUid")

    with open(CURR_URL+"/users.csv", "r") as users_csv_read:
      reader = csv.DictReader(users_csv_read)
      for row in reader:
        if row["email"] == email:
          break
      else:
        with open(CURR_URL+"/users.csv", "a") as users_csv_append:
          writer = csv.DictWriter(users_csv_append, fieldnames=["email","password","uid"])
          writer.writerow({
            "email": email,
            "password": pwd_h,
            "uid": uid
          })
        return "User inserted successfully"
      return "User already exists"

  
  return render_template("register.html")

@app.route("/userinfo")
@authenticated
def userinfo():
  email = session["email"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, uid=uid)

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. read the csv file and check if email/password match
#  3. if there is a match redirect to userinfo
@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["tbxEmail"]
    pwd = request.form["tbxPwd"]
    pwd_h = hashlib.sha256(pwd.encode()).hexdigest()

    with open(CURR_URL+"/users.csv", "r") as users_csv_read:
      reader = csv.DictReader(users_csv_read)
      for row in reader:
        if row["email"] == email and row["password"] == pwd_h:
          # user found and logged in successfully
          session["email"] = email
          session["uid"] = row["uid"]
          session["loggedin"] = True
          return redirect(url_for('userinfo'))
      return render_template("login.html")
  return render_template("login.html")

@app.route("/logout")
@authenticated
def logout():
  session["loggedin"] = False
  del session["loggedin"]
  session.clear()
  return redirect(url_for('login'))

if __name__ == "__main__":
  app.run(debug=True)