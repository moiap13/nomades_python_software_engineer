import os
import csv
import hashlib
from uuid import uuid4
from functools import wraps

from flask import Flask, render_template, request, session, redirect, url_for, flash
from dotenv import dotenv_values

from forms.login import Register, Login
from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = dotenv_values(os.path.join(CURR_DIR, ".env"))["SECRET_KEY"]

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not session.get("loggedin", False):
      flash("Please login first", "danger")
      return redirect(url_for("login"))
    return func(*args, **kwargs)
  return inner


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  register_form = Register(request.form, data=request.files)
  error: str = ""
  if request.method == "POST" and register_form.validate():
    uid: str = register_form.uid.data
    pwd: str = register_form.pwd.data
    firstname: str = register_form.firstname.data
    lastname: str = register_form.lastname.data
    email: str = register_form.email.data
    age: str = register_form.age.data
    profile_picture = register_form.profile_picture.data

    with open(CSV_FILE, "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        if (
          user.get("uid", "").lower() == uid.lower()
          or user.get("email", "") == email.lower()
        ):
          error = "User ID or Email already exists"
          return render_template('login/register.html', form=register_form, error=error)

    with open(CSV_FILE, mode="a") as users_csv_file:
      csv_writer = csv.writer(users_csv_file)
      salt: str = generate_password(True, True, False, False, 10)
      pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()

      pp_filename: str = f"{uuid4()}.{profile_picture.filename.split('.')[-1]}"
      profile_picture.save(os.path.join(UPLOADS_DIR, pp_filename))

      csv_writer.writerow([uid, pwd_h, salt, firstname, lastname, age, email, pp_filename])

      session["loggedin"] = True
      session["firstname"] = firstname
      session["lastname"] = lastname
      session["email"] = email
      session["age"] = age
      session["profile_picture_filename"] = pp_filename
      session["uid"] = uid

      flash("Successfully registered", "success")
      return redirect(url_for('user_info'))

  return render_template('login/register.html', form=register_form, error=error)
@app.route("/login", methods=["GET", "POST"])
def login():
  login_form = Login(request.form)
  error: str = ""
  if request.method == "POST":
    uid_email: str = login_form.uid.data
    pwd: str = login_form.pwd.data

    with open(CSV_FILE, "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        if user.get("uid", "") == uid_email or user.get("email") == uid_email:
          salt: str = user.get("salt", "")
          pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
          if user.get("pwd", "") == pwd_h:
            session["loggedin"] = True
            session["firstname"] = user["firstname"]
            session["lastname"] = user["lastname"]
            session["email"] = user["email"]
            session["age"] = user["age"]
            session["profile_picture_filename"] = user["profile_picture_filename"]
            session["uid"] = uid_email

            flash("Login sucessfull", "success")
            return redirect(url_for('user_info'))

    error = "Wrong Credentials"

  return render_template("login/login.html", form=login_form, error=error)

@app.route("/logout")
def logout():
  session.clear()
  flash("Logout successfull", "success")
  return redirect(url_for('login'))

@app.route("/user_info")
@authenticated(role=["user", "admin"])
def user_info():
  return render_template(
    "users/user_info.html",
    profile_picture_filename=session["profile_picture_filename"],
    firstname=session["firstname"],
    lastname=session["lastname"],
    email=session["email"],
    age=session["age"],
    uid=session["uid"]
  )
 
@app.route("/protected")
@authenticated
def protected():
  return "Protected route"

@app.route("/private")
@authenticated
def private():
  return "private"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)