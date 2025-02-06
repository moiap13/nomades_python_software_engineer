import os
import csv
import hashlib
import uuid

from flask import Flask, render_template, request, redirect, url_for, session, flash

from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

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

    if pwd != pwd_2:
      error = "The passwords doesn't match"
      return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, "r") as user_csv_file:
      csv_users: list[dict] = csv.DictReader(user_csv_file)
      for user in csv_users:
        if (user.get("uid", "").lower() == uid.lower()
            or user.get("emai", "") == email
        ):
          error = "The user id or email is already in use"
          return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, mode="a") as users_csv_file:
      csv_writer = csv.writer(users_csv_file)
      salt: str = generate_password(True, True, False, False, 10)
      pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
      
      pp_filename: str = f"{uuid.uuid4()}.{profile_picture.filename.split('.')[-1]}"
      profile_picture.save(os.path.join(UPLOADS_DIR, pp_filename))

      csv_writer.writerow([uid, pwd_h, salt, firstname, lastname, age, email, pp_filename])

      session["loggedin"] = True
      session["firstname"] = firstname
      session["lastname"] = lastname
      session["email"] = email
      session["age"] = age
      session["profile_picture"] = pp_filename
      session["uid"] = uid

      flash("Successfully registered", "success")
      return redirect(url_for("user_info"))

  return render_template('login/register.html', error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
  error: str = ""
  if request.method == "POST":
    uid_email: str = request.form.get("tbx_uid", "")
    print(uid_email)
    pwd: str = request.form.get("tbx_pwd", "")

    if not uid_email or not pwd:
      error = "Please fill out the form"
      return render_template('login/login.html', error=error)
    
    with open(CSV_FILE, "r") as user_csv_file:
      csv_users: list[dict] = csv.DictReader(user_csv_file)

      for user in csv_users:
        if user.get("uid", "") == uid_email or user.get("email", "") == uid_email:
          salt = user.get("salt", "")
          pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
          if user.get("pwd", "") == pwd_h:
            session["loggedin"] = True
            session["firstname"] = user["firstname"]
            session["lastname"] = user["lastname"]
            session["email"] = user["email"]
            session["age"] = user["age"]
            session["profile_picture"] = user["profile_picture_filename"]
            session["uid"] = uid_email

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
    firstname=session["firstname"],
    lastname=session["lastname"],
    email=session["email"],
    age=session["age"],
    profile_picture_filename=session["profile_picture"],
    uid=session["uid"]
  )

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)