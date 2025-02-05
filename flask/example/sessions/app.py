import os
import csv
import hashlib

from flask import Flask, render_template, request, session, redirect, url_for, flash
from dotenv import dotenv_values

from forms.login import Register, Login
from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")

env_config = dotenv_values(os.path.join(CURR_DIR, ".env"))

app = Flask(__name__)
app.config["SECRET_KEY"] = env_config.get("SECRET_KEY")

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  register_form = Register(request.form)
  error: str = ""
  if request.method == "POST" and register_form.validate():
    uid: str = register_form.uid.data
    pwd: str = register_form.pwd.data

    with open(CSV_FILE, "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        if user.get("uid", "").lower() == uid.lower():
          error = "User ID already exists"
          return render_template('login/register.html', form=register_form, error=error)

    with open(CSV_FILE, mode="a") as users_csv_file:
      csv_writer = csv.writer(users_csv_file)
      salt: str = generate_password(True, True, False, False, 10)
      pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
      csv_writer.writerow([uid, pwd_h, salt])

      session["uid"] = uid
      session["loggedin"] = True

      flash("Successfully Registered", "success")
      return redirect(url_for("user_info"))

  return render_template('login/register.html', form=register_form, error=error)
@app.route("/login", methods=["GET", "POST"])
def login():
  login_form = Login(request.form)
  error: str = ""
  if request.method == "POST":
    uid: str = login_form.uid.data
    pwd: str = login_form.pwd.data

    with open(CSV_FILE, "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        if user.get("uid", "") == uid:
          salt: str = user.get("salt", "")
          pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
          if user.get("pwd", "") == pwd_h:
            session["uid"] = uid
            session["loggedin"] = True
            flash("Successfully logged in", "success")
            return redirect(url_for("user_info"))

    error = "Wrong Credentials"

  return render_template("login/login.html", form=login_form, error=error)

@app.route("/logout")
def logout():
  session["loggedin"] = False
  session.pop("loggedin")
  # del session["loggedin"]
  session.clear()

  flash("Successfully logged out", "success")
  return redirect(url_for("login"))

@app.route("/user_info")
def user_info():
  return render_template("users/user_info.html", uid=session.get("uid", ""))

@app.route("/private")
def private():
  if not session.get("loggedin", False):
    return redirect(url_for("login"))

  return "I'm private, only logged users can see me"
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)