import os
import csv
import hashlib
import uuid

from flask import Flask, render_template, request

from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

app = Flask(__name__, template_folder="src")

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
    # TODO: get all the inputs from the user (firstname, lastname, age, email, profile_picture)

    # if uid == "" or pwd == "" or pwd_2 == "":
    if not uid or not pwd or not pwd_2:
      error = "Please fill out the form"
      return render_template('login/register.html', error=error)
    
    if pwd != pwd_2:
      error = "The passwords doesn't match"
      return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, "r") as user_csv_file:
      csv_users: list[dict] = csv.DictReader(user_csv_file)
      for user in csv_users:
        if user.get("uid", "") == uid:
          error = "The user id is already in use"
          return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, mode="a") as users_csv_file:
      csv_writer = csv.writer(users_csv_file)
      salt: str = generate_password(True, True, False, False, 10)
      pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
      csv_writer.writerow([uid, pwd_h, salt])
      # TODO: redirect to user_info
      return "successfully inserted"

  return render_template('login/register.html', error=error)

@app.route("/login", methods=["GET", "POST"])
def login():
  error: str = ""
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")

    if not uid or not pwd:
      error = "Please fill out the form"
      return render_template('login/login.html', error=error)
    
    with open(CSV_FILE, "r") as user_csv_file:
      csv_users: list[dict] = csv.DictReader(user_csv_file)

      for user in csv_users:
        if user.get("uid", "") == uid:
          salt = user.get("salt", "")
          pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
          if user.get("pwd", "") == pwd_h:
            # TODO: find a way for storing user data
            # TODO: redirect to user_info
            return "Login Successfull"
    
    error = "Wrong credentials" 
 
  return render_template("login/login.html", error=error)

# TODO: Implement logout route

# TODO: cretae user info route accessible via GET
# TODO: This route should be protected by login (if not logged -> redirect to login)
# TODO: This route only returns the user_info.html template, and use the values for the user given from the CSV

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)