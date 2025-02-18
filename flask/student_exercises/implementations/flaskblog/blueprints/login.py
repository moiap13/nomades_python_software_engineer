import os, sys

import hashlib
import uuid

from flask import Blueprint, request, render_template, session, flash, redirect, url_for

CURR_DIR: str = os.path.dirname(__file__)
ROOT_DIR: str = os.path.dirname(CURR_DIR)
UPLOADS_DIR: str = os.path.join(ROOT_DIR, "static", "uploads")

sys.path.append(ROOT_DIR)

from forms.login import RegisterForm, LoginForm
from helpers.random_password_generator import generate_password
from config.firestore_db import db

login_bp = Blueprint("login", __name__)

@login_bp.route("/register", methods=["GET", "POST"])
def register():
  register_form = RegisterForm(request.form, data=request.files)
  error: str = ""
  if request.method == "POST" and register_form.validate():
    uid: str = register_form.uid.data
    pwd: str = register_form.pwd.data
    firstname: str = register_form.firstname.data
    lastname: str = register_form.lastname.data
    email: str = register_form.email.data
    age: int = register_form.age.data
    profile_picture = register_form.profile_picture.data
    
    if profile_picture.content_type.split("/")[0] != "image": # audio/mp3
      error = "Please upload an image file"
      return render_template('login/register.html', form=register_form, error=error)

    if uid == email:
      error = "Please choose an user id and email with different values"
      return render_template('login/register.html', form=register_form, error=error)

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

    _, doc_ref = db.collection(u"users").add(user_dict)

    user_data: dict[str, str | int] = user_dict.copy()
    user_data.pop("salt")
    user_data.pop("password")
    user_data["id"] = doc_ref.id
    
    session["loggedin"] = True
    session["user"] = user_data

    flash("Successfully registered", "success")
    return redirect(url_for("user.user_info"))

  return render_template('login/register.html', error=error, form=register_form)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
  error: str = ""
  login_form = LoginForm(request.form)
  if request.method == "POST" and login_form.validate():
    uid_email: str = login_form.uid_email.data
    pwd: str = login_form.pwd.data

    users_with_email: list[firestore.DocumentSnapshot] = db.collection(u"users").where("email", "==", uid_email).get()
    users_with_uid: list[firestore.DocumentSnapshot] = db.collection(u"users").where("uid", "==", uid_email).get()

    for user in (users_with_email+users_with_uid):
      user_data: dict[str, str|int] = user.to_dict()
      h_pwd: str = hashlib.sha256((pwd+user_data.get("salt", "")).encode("utf-8")).hexdigest()
      if h_pwd == user_data.get("password", ""):
        session["loggedin"] = True
        user_data.pop("salt")
        user_data.pop("password")
        user_data["id"] = user.id
        session["user"] = user_data 

      flash("Login sucessfull", "success")
      return redirect(url_for("user.user_info")) 

    error = "Wrong credentials" 
 
  return render_template("login/login.html", error=error, form=login_form)

@login_bp.route("/logout")
def logout():
  session.clear()
  return redirect(url_for("login.login"))
