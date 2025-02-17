import os
import csv
import hashlib
import uuid

from flask import Flask, render_template, request, redirect, url_for, session, flash
import firebase_admin
from firebase_admin import credentials, firestore

from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

cred = credentials.Certificate(os.path.join(CURR_DIR, 'config', "firestore-creds.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

app = Flask(__name__, template_folder="src")
app.config["SECRET_KEY"] = "secret"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  error: str = ""
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")
    pwd_2: str = request.form.get("tbx_pwd_2", "")
    firstname: str = request.form.get("tbx_firstname", "")
    lastname: str = request.form.get("tbx_lastname", "")
    email: str = request.form.get("tbx_email", "")
    age: str = request.form.get("tbx_age", "")
    profile_picture = request.files.get("input_pp")

    # if uid == "" or pwd == "" or pwd_2 == "":
    if (
      not uid or not pwd or not pwd_2 or not firstname 
      or not lastname or not email or not age
    ):
      error = "Please fill out the form"
      return render_template('login/register.html', error=error)

    if profile_picture.content_type.split("/")[0] != "image": # audio/mp3
      error = "Please upload an image file"
      return render_template('login/register.html', error=error)

    if uid == email:
      error = "Please choose an user id and email with different values"
      return render_template('login/register.html', error=error) 

    if pwd != pwd_2:
      error = "The passwords doesn't match"
      return render_template('login/register.html', error=error)

    users_with_email: list[firestore.DocumentSnapshot] = db.collection(u"users").where("email", "==", email).get()
    users_with_uid: list[firestore.DocumentSnapshot] = db.collection(u"users").where("uid", "==", uid).get()

    if len(users_with_email + users_with_uid) > 0:
     error = "The user id or email is already in use"
     return render_template('login/register.html', error=error)

    salt: str = generate_password(True, True, False, False, 10)
    h_pwd: str = hashlib.sha256((pwd+salt).encode("utf-8")).hexdigest()
    pp_filename: str = f"{uuid.uuid4()}.{profile_picture.filename.split('.')[-1]}"
    profile_picture.save(os.path.join(UPLOADS_DIR, pp_filename)) 

    user_dict: dict[str, str | int] = {
      "firstname": firstname,
      "lastname": lastname,
      "uid": uid,
      "email": email,
      "age": age,
      "profile_picture_filename": pp_filename,
      "salt": salt,
      "password": h_pwd
    }

    db.collection(u"users").add(user_dict)

    user_data: dict[str, str | int] = user_dict.copy()
    user_data.pop("salt")
    user_data.pop("password")
    
    session["loggedin"] = True
    session["user"] = user_data

    flash("Successfully registered", "success")
    return redirect(url_for("user_info"))

  return render_template('login/register.html', error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
  error: str = ""
  if request.method == "POST":
    uid_email: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")

    if not uid_email or not pwd:
      error = "Please fill out the form"
      return render_template('login/login.html', error=error)
  
    # for user in db.collection(u"users").stream():
    #   user_data: dict[str, str|int] = user.to_dict()
    #   if (
    #     user_data.get("uid", "") == uid_email 
    #     or user_data.get("email", "") == uid_email
    #   ):
    #     h_pwd: str = hashlib.sha256((pwd+user_data.get("salt", "")).encode("utf-8")).hexdigest()
    #     if h_pwd == user_data.get("password", ""):
    #      session["loggedin"] = True
    #      user_data.pop("salt")
    #      user_data.pop("password")
    #      session["user"] = user_data 

    #     flash("Login sucessfull", "success")
    #     return redirect(url_for("user_info"))

    users_with_email: list[firestore.DocumentSnapshot] = db.collection(u"users").where("email", "==", uid_email).get()
    users_with_uid: list[firestore.DocumentSnapshot] = db.collection(u"users").where("uid", "==", uid_email).get()

    for user in (users_with_email+users_with_uid):
      user_data: dict[str, str|int] = user.to_dict()
      h_pwd: str = hashlib.sha256((pwd+user_data.get("salt", "")).encode("utf-8")).hexdigest()
      if h_pwd == user_data.get("password", ""):
        session["loggedin"] = True
        user_data.pop("salt")
        user_data.pop("password")
        session["user"] = user_data 

      flash("Login sucessfull", "success")
      return redirect(url_for("user_info")) 

    error = "Wrong credentials" 
 
  return render_template("login/login.html", error=error)

@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("login"))

@app.route("/user_info")
def user_info():
  if not session.get("loggedin", False):
    flash("Please log in first", "danger")
    return redirect(url_for("login"))
  
  return render_template(
    "users/user_info.html", 
    user=session["user"]
  )

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)