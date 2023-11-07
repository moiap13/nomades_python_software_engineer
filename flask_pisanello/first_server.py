from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

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
def user_info():
  print(session["email"])
  return render_template("userinfo.html", email=session["email"], pwd=session["pwd"])

@app.route("/forms", methods=["GET", "POST"])
def test_forms():
    if request.method == "POST":
      #TODO:get email and password
      # do the post things
      email:str = request.form["tbxEmail"]
      pwd:str = request.form["tbxPwd"]
      session["email"] = email
      session["pwd"] = pwd
      print(session["email"])

      #TODO: Open csv file
      #TODO: check if email + password is a valid credentilal gien csv data
      
      # if credential is accepted ->  store in session the uid from csv file
      #                               return "logged"
      # else -> return render_template("forms/form.html")

      return ""
    else:
      # Get will return the template
      return render_template("forms/form.html")
  
@app.route("/check_uid")
def check_uid():
  if "uid" in session:
    return session["uid"]
  return "Login first to store the uid please !"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)