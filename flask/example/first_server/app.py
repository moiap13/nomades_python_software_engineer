from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/")
def index() -> str:
 return "<h1>Hello PPL !</h1><img src='https://en.wikipedia.org/static/images/icons/wikipedia.png'>"

@app.route("/hello/<name>/<name2>")
def hello_name(name: str, name2: str) -> str:
  print(type(name))
  return f"<h1>Hello <span style='color: red'>{name}</span></h1><h2>{name2}</h2>"

@app.route("/hello/<name>/<int:age>")
def hello_age(name: str, age: int) -> str:
  return f"<h1>Hello <span style='color: red'>{name}</span></h1><p>You are {age} years old</p>"

@app.route('/allow/<int:age>')
def allow_voting(age):
    return "You are allowed to enter the voting website" if age >= 18 else "You are not allowed to enter the voting website"

################################################################################
################################### FORMS ######################################
################################################################################

@app.route("/user_info", methods=["GET", "POST"])
def user_info() -> str:
  if request.method == "POST":
    firstname: str = request.form.get("tbx_firstname", "")
    lastname: str = request.form.get("tbx_lastname", "")
    email: str = request.form.get("tbx_email", "")
    age: str = request.form.get("tbx_age", "")

    if firstname == "" or not firstname.isalpha() or len(firstname) < 2:
      return render_template("forms/user_info.html") 

    return render_template(
      "views/user_info.html",
      firstname=firstname, 
      lastname=lastname,
      email=email,
      age=age
    )
  else:
    return render_template("forms/user_info.html")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)