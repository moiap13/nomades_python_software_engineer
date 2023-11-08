from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
from wtforms import Form, validators, StringField, PasswordField, EmailField, IntegerField

class Login(Form):
  email = EmailField('Email', [validators.input_required(), validators.email()])
  password = PasswordField('Password', [validators.input_required()])

class SignUp(Form):
  firstname = StringField('Enter Firstname', [validators.input_required(), validators.length(2, 10)])
  lastname = StringField('Lastname', [validators.input_required(), validators.length(2, 10)])
  email = EmailField('Email', [validators.input_required(), validators.email()])
  age = IntegerField("Age", [validators.NumberRange(13, 20)])
  uid = StringField("User-Id", [validators.input_required(), validators.length(3, 5, "le user id doit être compris entre 3 et 5 charactères")])
  password = PasswordField('Password', [validators.data_required(), validators.equal_to('confirm',message='PASSWORDS DONT MATCH')])
  confirm = PasswordField('Confirm password')

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("logged" in session and session["logged"]):
      return redirect(url_for('login'))
    
    assert session["logged"]
    return func(*args, **kwargs)
  return inner

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/hello/<name>')
def index_3(name):
  # computation part
  b: bool = name == "antonio"

  # rendering part
  parameter = {
    "name": name,
    "nameMaj": name.upper(),
    "b": b,
    "fruits": ["apple", "banana", "watermelon", "orange"],
    "html": "<script>alert('hello')</script>"
  }
  return render_template("hello/hello.html", parameter=parameter)

@app.route("/add/<int:n1>/<n2>")
def add(n1, n2):
  session["email"] = "default@email.com"
  session["pwd"] = "defaultPwd"
  return str(n1)+n2

@app.route("/userinfo")
@authenticated
def user_info():
  return render_template("userinfo.html", email=session["email"], pwd=session["pwd"], uid=session["uid"])

@app.route("/log_in", methods=["GET", "POST"])
def login():
    if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
    
    if request.method == "POST":
      import csv

      #TODO:get email and password
      # do the post things
      email:str = request.form["tbxEmail"]
      pwd:str = request.form["tbxPwd"]
      session["email"] = email
      session["pwd"] = pwd  
      print(session["email"])

      #TODO: Open csv file
      user_records = []
      with open("users.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        user_records = [(row) for row in reader]
      #TODO: check if email + password is a valid credentilal gien csv data
      for user_data in user_records:
        if user_data[0] == email and user_data[1] == pwd:
          session["logged"] = True
          session["uid"] = user_data[2]
          return "logged"
        
      return render_template("forms/form.html", error='uid and pwd doesnt match')
      
      # if credential is accepted ->  store in session the uid from csv file
      #                               return "logged"
      # else -> return render_template("forms/form.html")

      return ""
    else:
      # Get will return the template
      return render_template("forms/form.html", error="")
    
@app.route("/login_wtf", methods=["GET", "POST"])
def login_wtf():
    if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
    
    login_form = Login(request.form)

    if request.method == "POST" and login_form.validate():
      import csv

      #TODO:get email and password
      # do the post things
      email:str = login_form.email.data
      pwd:str = login_form.password.data
      session["email"] = email
      session["pwd"] = pwd  
      print(session["email"])

      #TODO: Open csv file
      user_records = []
      with open("users.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        user_records = [(row) for row in reader]
      #TODO: check if email + password is a valid credentilal gien csv data
      for user_data in user_records:
        if user_data[0] == email and user_data[1] == pwd:
          session["logged"] = True
          session["uid"] = user_data[2]
          return redirect(url_for("user_info"))
        
      return render_template("forms/form.html", error='uid and pwd doesnt match')
    
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

    with open("users.csv", "a") as f:
      writer = csv.writer(f)
      writer.writerow([email, pwd, uid])
    
    session["logged"] = True
    session["uid"] = uid
    
    return "User created !"
  else:
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

    with open("users.csv", "a") as f:
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

  
@app.route("/check_uid")
def check_uid():
  if "uid" in session:
    return session["uid"]
  return "Login first to store the uid please !"

@app.route("/secret")
@authenticated
def secret():
  return "secret"

@app.route("/secret2")
@authenticated
def secret_2():
  return "secret 2"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)