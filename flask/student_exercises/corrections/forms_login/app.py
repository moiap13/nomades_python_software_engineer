from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
import csv
import hashlib
import string
import random

CURR_DIR: str = os.path.dirname(__file__)
USERS_CSV_PATH: str = f"{CURR_DIR}/users_h_salted.csv"

app = Flask(__name__)
# app.secret_key = "secret"
app.config["SECRET_KEY"] = "some_secret"

def authenticate(f):
  @wraps(f)
  def inner_func(*args, **kwargs):
    if not session.get("loggedin", False):
      flash("login first", "warning")
      return redirect(url_for("login"))
    
    return f(*args, **kwargs)
  return inner_func


@app.route("/")
def index():
  return render_template("index.html", active_link="a_home")

@app.route("/register", methods=["POST", "GET"])
def register():
  if request.method == "POST":
    email: str = request.form["tbxEmail"]
    pwd: str = request.form["tbxPwd"]
    uid: str = request.form["tbxUid"]
    all_chars: str = string.ascii_letters + string.digits
    salt: str = "".join(random.choices(all_chars, k=10))
    h_pwd: str = hashlib.sha256((pwd+salt).encode()).hexdigest()

    with open(USERS_CSV_PATH) as users_file:
      reader = csv.DictReader(users_file)
      if any([user_dict["email"] == email for user_dict in reader]):
        flash('Email already in use', "danger")
        return render_template("login/register.html", active_link="a_register")

    with open(USERS_CSV_PATH, "a") as users_file:
      writer = csv.writer(users_file)
      writer.writerow([email, h_pwd, uid, salt])

    session["loggedin"] = True
    session["email"] = email
    session["pwd"] = pwd
    session["uid"] = uid

    flash('Successfully registered', 'success')

    return redirect(url_for("userinfo"))

  return render_template("login/register.html", active_link="a_register")

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email: str = request.form["tbxEmail"]
    pwd: str = request.form["tbxPwd"]

    with open(USERS_CSV_PATH) as users_file:
      reader = csv.DictReader(users_file)
      for user_dict in reader:
        h_pwd: str = hashlib.sha256((pwd+user_dict["salt"]).encode()).hexdigest()
        if email == user_dict["email"] and h_pwd == user_dict["password"]:
          session["loggedin"] = True
          session["email"] = email
          session["pwd"] = pwd
          session["uid"] = user_dict["uid"]

          flash('Login successfull', 'success')
          return redirect(url_for("userinfo"))
        
    flash('Wrong crendentials', 'danger')

  return render_template("login/login.html", active_link="a_login")

@app.route("/logout")
@authenticate
def logout():
  session["loggedin"] = False
  return redirect(url_for("login"))

@app.route("/user/info/")
@authenticate
def userinfo():
  email: str = session.get("email", "")
  pwd: str = session.get("pwd", "")
  uid: str = session.get("uid", "")
  return render_template("userinfo.html", email=email, password=pwd, uid=uid, active_link="a_userinfo")

@app.route("/secret")
@authenticate
def secret():
  return "this is a secret part of the website"

if __name__ == "__main__":
  app.run(port=8080, debug=True)