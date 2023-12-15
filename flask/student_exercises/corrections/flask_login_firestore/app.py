from flask import Flask, render_template, request, session, redirect, url_for
import os
import csv
import hashlib
from functools import wraps
import firebase_admin
from firebase_admin import credentials, firestore

USER_COLLECTION = u"users_loggin_ex"

CURR_URL = os.path.dirname(__file__)
app = Flask(__name__)
app.secret_key = "secret"

cred = credentials.Certificate(f"./firebase_cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("loggedin" in session and session["loggedin"]):
      return redirect(url_for('login'))
    
    assert session["loggedin"]
    return func(*args, **kwargs)
  return inner

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then open a csv file and add the new user
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of th e input
    password = request.form.get("tbxPwd")
    pwd_h = hashlib.sha256(password.encode()).hexdigest()
    uid = request.form.get("tbxUid")
    
    new_user = {
      "email": email,
      "password": pwd_h,
      "uid": uid
    }

    
    _, document_ref = db.collection(USER_COLLECTION).add(new_user)
    session["doc_id"] = document_ref.id 
    session["loggedin"] = True
    return redirect(url_for('userinfo'))
  
  return render_template("register.html")

@app.route("/userinfo")
@authenticated
def userinfo():
  print(session)
  user = db.collection(USER_COLLECTION).document(session["doc_id"]).get().to_dict()
  return render_template("userinfo.html", email=user["email"], uid=user["uid"])

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. read the csv file and check if email/password match
#  3. if there is a match redirect to userinfo
@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    email = request.form["tbxEmail"]
    pwd = request.form["tbxPwd"]
    pwd_h = hashlib.sha256(pwd.encode()).hexdigest()

    users = db.collection(USER_COLLECTION).stream()
    for user_doc_ref in users:
      user_values = user_doc_ref.to_dict()

      if user_values["email"] == email and user_values["password"] == pwd_h:
        session["doc_id"] = user_doc_ref.id
        session["loggedin"] = True
        return redirect(url_for('userinfo'))

  return render_template("login.html")

@app.route("/logout")
@authenticated
def logout():
  session["loggedin"] = False
  del session["loggedin"]
  session.clear()
  return redirect(url_for('login'))

if __name__ == "__main__":
  app.run(debug=True)