from flask import Flask, render_template, request, session, redirect, url_for
from common import authenticated
from common.forms import Login, SignUp
import os

#TODO: add firestore imports

CURR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURR_DIR, "static/data")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

#TODO: create firestore instance (connection with credentials and instatiation of db object)

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
  
  login_form = Login(request.form)

  if request.method == "POST" and login_form.validate():
    #TODO: Login using firebase documents instead of csv files
    email:str = login_form.email.data
    pwd:str = login_form.password.data
      
  return render_template("login/login.html", form=login_form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
  
  signup_form = SignUp(request.form)

  if request.method == "POST" and signup_form.validate():
    fn = signup_form.firstname.data
    ln = signup_form.lastname.data
    email = signup_form.email.data
    age = signup_form.age.data
    uid = signup_form.uid.data
    pwd = signup_form.password.data

    # TODO: add new docuement un firestore containing the user data. if email is not already used in database
  else:
    return render_template("login/signup.html", form=signup_form)
@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('index'))

# TODO: Post things: view_post, view_posts and create_post using the firestore database.
# TODO: Perform the search on post using the attributes: title, content and categories in the firestore database

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)