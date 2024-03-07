import csv
from flask import Flask, render_template, request, session, redirect, url_for
from utils.decorators import authenticated, public
from forms.login import LoginForm, RegisterForm
import hashlib
import string
import random

# to install firebase_admin run (inside nomades_flask_310 env): pip isntall firebase_admin
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("key_cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

app = Flask(__name__)
app.secret_key = "secret"

all_chars = string.digits + string.ascii_letters + string.punctuation

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
@public
def register():
  error = ''
  if request.method == "POST":
    # TODO: Register using firestore
    # create new documents in the users collection (add() or set())
    # a user should have: email, password
    # feel free to add new data for the new registered user such as: firstname, lastname, etc...

    email: str = request.form["tbxEmail"]
    pwd: str = request.form["tbxPwd"]
    # salt: str = "".join(random.sample(all_chars, 10))
    #h_pwd = hashlib.sha256((salt+pwd).encode()).hexdigest()

    # no need to be changed to firestore
    last_uid: int = 0
    with open("users.csv", "r") as users_csv_read:
      rows = csv.reader(users_csv_read)
      next(rows)
      for row in rows:
        if email == row[0]:
          error = "Email already used please login"
          return render_template("register.html", error=error) 
    
        last_uid = int(row[2])
    last_uid += 1

    with open("users.csv", "a") as users_csv_add:
      writer = csv.writer(users_csv_add)
      # writer.writerow([email, h_pwd, last_uid, salt])
      writer.writerow([email, pwd, last_uid])

    session["logged"] = True
    session["email"] = email
    session["password"] = pwd
    session["uid"] = last_uid
    return redirect(url_for('userinfo'))
  
  # GET
  return render_template("register.html")

@app.route("/user/info")
@authenticated
def userinfo():
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, password=password, uid=uid)

@app.route("/login", methods=["GET", "POST"])
@public
def login():
  # TODO: Login using firestore
  # get all the documents from the collection users using stream()
  # loop throught all documents and check if email and pwd match
  error = ''
  form = LoginForm(request.form)
  if request.method == "POST" and form.validate():
    email: str = form.email.data
    pwd: str = form.pwd.data

    with open("users.csv", "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        salt = user["salt"]
        #h_pwd = hashlib.sha256((salt+pwd).encode()).hexdigest()
        if user.get("email") == email and user.get("password") == pwd: #h_pwd:
          # Le user est reconnu 
          # Je vais stocker des infos en mémoire (session)
          session["logged"] = True
          session["email"] = email
          session["password"] = pwd
          session["uid"] = user.get("uid") # document id
          return redirect(url_for('userinfo'))
      error = 'email / pwd: doesn\'t match'
  
  # GET
  return render_template("login_wtf.html", error=error, form=form)

@app.route("/logout")
@authenticated
def logout():
  session.clear()
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)