import os
import csv
import hashlib

from flask import Flask, render_template, request, session, redirect, url_for, flash

from helpers.random_password_generator import generate_password

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOAD_DIR: str = os.path.join(CURR_DIR, "uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = "big_secret"

@app.route("/")
def index():
  return render_template("index.html")
  
@app.route("/files", methods=["GET", "POST"])
def files():
  if request.method == "POST":
    files = request.files.getlist("fileInput")
    for file in files:
      if file.content_type.split("/")[0] == "image":
        print(file.content_type)
        ext: str = file.filename.split(".")[-1]
        file_path: str = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.{ext}")
        file.save(file_path)
    return f"File successfully saved id {file_path}"

  return render_template("forms/sending_files.html")

################################################################################
################################## LOGIN #######################################
################################################################################

@app.route("/signup", methods=["GET", "POST"])
def register():
  error: str = ""
  if request.method == "POST":
    uid: str = request.form.get("tbx_uid", "")
    pwd: str = request.form.get("tbx_pwd", "")
    pwd_2: str = request.form.get("tbx_pwd_2", "")

    # if uid == "" or pwd == "" or pwd_2 == "":
    if not uid or not pwd or not pwd_2:
      error = "Please fill out the form"
      return render_template('login/register.html', error=error)
    
    if pwd != pwd_2:
      error = "The passwords doesn't match"
      return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, "r") as user_csv_file:
      csv_users = csv.DictReader(user_csv_file)
      for user in csv_users:
        if user.get("uid", "") == uid:
          error = "The user id is already in use"
          return render_template('login/register.html', error=error)
    
    with open(CSV_FILE, mode="a") as users_csv_file:
      csv_writer = csv.writer(users_csv_file)
      salt: str = generate_password(True, True, False, False, 10)
      pwd_h: str = hashlib.sha256((pwd+salt).encode()).hexdigest()
      csv_writer.writerow([uid, pwd_h, salt])

      session["uid"] = uid
      session["loggedin"] = True
      redirect(url_for("user_info"))

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
            session["uid"] = uid
            session["loggedin"] = True
            flash("Login successfull", "success")
            return redirect(url_for("user_info"))
    
    error = "Wrong credentials"
 
  return render_template("login/login.html", error=error)

@app.route("/logout")
def logout():
  session["loggedin"] = False
  del session["loggedin"]
  session.clear()
  return redirect(url_for("login"))

@app.route("/user_info")
def user_info():
  return render_template("views/user_info.html", uid=session.get("uid", ""))

@app.route("/private")
def private():
  if not session.get("loggedin", False):
    return redirect(url_for('login'))

  return "I'm a private route, only logged users can see me"

################################################################################
################################## SESSION #####################################
################################################################################

@app.route("/session")
def s():
  print(session)
  return session.get("uid", "")
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)