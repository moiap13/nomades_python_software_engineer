from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
  return "Hello"

@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    email = request.form["tbxEmail"]
    password = request.form["tbxPwd"]
    uid = request.form["tbxUid"]

    session["email"] = email
    session["password"] = password
    session["uid"] = uid

    return redirect(url_for("userinfo"))
  
  return render_template("register.html")

@app.route("/userinfo")
def userinfo():
  email = session["email"]
  password = session["password"]
  uid = session["uid"]
  return render_template("userinfo.html", email=email, passwod=password, uid=uid)

if __name__ == "__main__":
  app.run(debug=True)