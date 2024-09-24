from flask import Flask, render_template, request, session, redirect, url_for, flash
import os
import csv
import hashlib
from functools import wraps
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import string
import random

CURR_URL = os.path.dirname(__file__)

cred = credentials.Certificate(os.path.join(CURR_URL, "database", "firebase_login-creds.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
app.secret_key = "secret"

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
    salt: str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    pwd_h = hashlib.sha256((salt+password).encode()).hexdigest()
    uid = request.form.get("tbxUid")

    user_w_email = db.collection(u"users").where("email", "==", email).get()

    if len(user_w_email) == 0:
      _, u = db.collection(u"users").add({
        "email": email,
        "password": pwd_h,
        "uid": uid,
        "salt": salt
      })
      flash("User inserted successfully", "success")

      session["loggedin"] = True
      session["firestore_id"] = u.id

      return redirect(url_for('userinfo'))
    else:
      flash("user already exists", "danger")
      
  return render_template("register.html")

@app.route("/userinfo")
@authenticated
def userinfo():
  u = db.collection(u'users').document(session['firestore_id']).get()
  u_data = u.to_dict()
  return render_template("userinfo.html", email=u_data["email"], uid=u_data['uid'])

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

    user_by_email: list = db.collection(u"users").where("email", "==", email).get()

    if len(user_by_email) > 0:
      user_doc = user_by_email[0]
      user_data: dict = user_doc.to_dict()
      salt: str = user_data["salt"]
      pwd_h: str = hashlib.sha256((salt+pwd).encode()).hexdigest()

      if pwd_h == user_data["password"]:
        flash("Login successful", "success")
        session["loggedin"] = True
        session["firestore_id"] = user_doc.id
        return redirect(url_for('userinfo'))

    flash("Wrong Crendentials", "danger")
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