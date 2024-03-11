import csv
from flask import Flask, render_template, request, session, redirect, url_for
from utils.decorators import authenticated, public

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
@public
def register():
  error = ''
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then open a csv file and add the new user
    email: str = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    pwd: str = request.form["tbxPwd"]

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
  # TODO: protect user info page
  # only logged in persons can acces to this route
  # use session to keep in memory if logged and values
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, password=password, uid=uid)

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. read the csv file and check if email/password match
#  3. if there is a match redirect to userinfo
@app.route("/login", methods=["GET", "POST"])
@public
def login():
  error = ''
  if request.method == "POST":
    email: str = request.form.get("tbxEmail")
    pwd: str = request.form.get("tbxPwd")

    with open("users.csv", "r") as users_csv_file:
      users = csv.DictReader(users_csv_file)
      for user in users:
        if user.get("email") == email and user.get("password") == pwd:
          # Le user est reconnu 
          # Je vais stocker des infos en mémoire (session)
          session["logged"] = True
          session["email"] = email
          session["password"] = pwd
          session["uid"] = user.get("uid")
          return redirect(url_for('userinfo'))
      error = 'email / pwd: doesn\'t match'
  
  # GET
  return render_template("login.html", error=error)


#TODO: create logout page
# logout should destroy the session
# redirect to Login
@app.route("/logout")
@authenticated
def logout():
  session.clear()
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)