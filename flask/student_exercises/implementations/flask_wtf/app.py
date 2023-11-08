from flask import Flask, render_template, request, session, redirect, url_for
from common import authenticated
from common.forms import Login, SignUp
import os

CURR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURR_DIR, "static/data")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/userinfo")
@authenticated
def user_info():
  return render_template("users/userinfo.html", email=session["email"], pwd=session["pwd"], uid=session["uid"])

@app.route("/login", methods=["GET", "POST"])
def login():
  if "logged" in session and session["logged"]:
    return redirect(url_for('user_info'))
  
  if request.method == "POST":
    import csv

    email:str = request.form["tbxEmail"]
    pwd:str = request.form["tbxPwd"]
    session["email"] = email
    session["pwd"] = pwd  
    print(session["email"])

    user_records = []
    with open(f"{DATA_DIR}/users.csv", "r") as f:
      reader = csv.reader(f)
      next(reader)
      user_records = [(row) for row in reader]

    for user_data in user_records:
      if user_data[0] == email and user_data[1] == pwd:
        session["logged"] = True
        session["uid"] = user_data[2]
        return "logged"
      
    return render_template("forms/form.html", error='uid and pwd doesnt match')

  return render_template("forms/form.html", error="")
    
@app.route("/login_wtf", methods=["GET", "POST"])
def login_wtf():
  if "logged" in session and session["logged"]:
    return redirect(url_for('user_info'))
  
  login_form = Login(request.form)

  if request.method == "POST" and login_form.validate():
    import csv

    email:str = login_form.email.data
    pwd:str = login_form.password.data
    session["email"] = email
    session["pwd"] = pwd  
    print(session["email"])

    user_records = []
    with open(f"{DATA_DIR}/users.csv", "r") as f:
      reader = csv.reader(f)
      next(reader)
      user_records = [(row) for row in reader]

    for csv_email, csv_pwd, csv_uid in user_records:
      if csv_email == email and csv_pwd == pwd:
        session["logged"] = True
        session["uid"] = csv_uid
        return redirect(url_for("user_info"))
      
  return render_template("forms/login_wtf.html", form=login_form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
  
  if request.method == "POST":
    import csv

    email:str = request.form["tbxEmail"]
    pwd:str = request.form["tbxPwd"]
    uid:str = request.form["tbxUid"]
    session["email"] = email
    session["pwd"] = pwd
    session["uid"] = uid

    with open(f"{DATA_DIR}/users.csv", "a") as f:
      writer = csv.writer(f)
      writer.writerow([email, pwd, uid])
    
    session["logged"] = True
    
    return redirect(url_for('user_info'))

  return render_template("forms/signup.html")
  
@app.route("/signup_wtf", methods=["GET", "POST"])
def signup_wtf():
  if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
  
  signup_form = SignUp(request.form)

  if request.method == "POST" and signup_form.validate():
    import csv

    fn = signup_form.firstname.data
    ln = signup_form.lastname.data
    email = signup_form.email.data
    age = signup_form.age.data
    uid = signup_form.uid.data
    pwd = signup_form.password.data

    with open(f"{DATA_DIR}/users.csv", "a") as f:
      writer = csv.writer(f)
      writer.writerow([email, pwd, uid])
    
    session["logged"] = True
    session["uid"] = uid
    
    return "User created !"
  else:
    return render_template("forms/signup_wtf.html", form=signup_form)
@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('index'))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)