from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    # TODO: get values from the form 
    # hint: user request.form
    # then open a csv file and add the new user
    email = request.form["tbxEmail"] # here be sure that the key of the dictionary is the NAME html attribute of the input
    return redirect(url_for("userinfo"))
  
  return render_template("register.html")

@app.route("/userinfo")
def userinfo():
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, passwod=password, uid=uid)

#TODO: create a route for login that can be accessed by GET and POST
# when acceding by get only return the login.html file
# when acceding by POST:
#  1. get the data from form
#  2. read the csv file and check if email/password match
#  3. if there is a match redirect to userinfo

if __name__ == "__main__":
  app.run(debug=True)