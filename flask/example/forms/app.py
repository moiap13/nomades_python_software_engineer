from flask import Flask, render_template, request, send_from_directory, send_file
import os
import uuid

from forms.user_info import UserInfo

app = Flask(__name__)

CURR_DIR: str = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR: str = os.path.join(CURR_DIR, "uploads")

@app.route("/")
def index() -> str:
  return render_template('index.html')

@app.route("/hello/<name>")
def hello(name: str) -> str:
  print(type(name))
  return f"<h1>Hello <span style='color: red'>{name}</span></h1>"

@app.route("/allow/<int:age>")
def age(age: int) -> str:
  return "You are allowed to vote using this website" if age >= 18 else "You are not able to vote using this website"

################################################################################
############################### FORMS ##########################################
################################################################################

@app.route("/user_info", methods=["GET", "POST"])
def user_info():
  if request.method == "POST":
    firstname: str = request.form.get("tbx_firstname", "")
    lastname: str = request.form.get("tbx_lastname", "")
    email: str = request.form.get("tbx_email", "")
    age: str = (request.form.get("tbx_age", ""))
    password: str = request.form.get("tbx_password", "")

    if firstname == "" or not firstname.isalpha() or len(firstname) < 2:
      return "Firstname should be valid"

    return render_template("views/user_info.html", 
                           firstname=firstname,
                           lastname=lastname,
                           email=email,
                           age=age)
  else:
    return render_template("forms/user_info.html")

@app.route("/files", methods=["GET", "POST"])
def file_sending():
  if request.method == "POST":
    files: list = request.files.getlist("fileInput")
    file_path = ""
    for file in files:
      if file.content_type.split("/")[0] == "image":
        ext: str = file.filename.split(".")[-1]
        file_path: str = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.{ext}")
        file.save(file_path)
    return f"file saved successfully in {file_path}"

  return render_template("forms/file_sending.html")

@app.route("/file/<file_name>")
def get_file(file_name: str):
  # return send_from_directory(UPLOAD_DIR, file_name)
  return send_file(os.path.join(UPLOAD_DIR, file_name), as_attachment=True)

################################################################################
############################ WTF FORMS #########################################
################################################################################

@app.route("/user_info_wtf", methods=["GET", "POST"])
def user_info_wtf():
  user_info_form = UserInfo(request.form)
  if request.method == "POST" and user_info_form.validate():
      firstname: str = user_info_form.firstname.data
      lastname: str = user_info_form.lastname.data
      email: str = user_info_form.email.data
      age: str = user_info_form.age.data
      gender: str = user_info_form.gender.data
      password: str = user_info_form.password.data
      print(type(age))
      print(gender, password)
      return render_template("views/user_info_wtf.html", form=user_info_form, firstname=firstname, lastname=lastname, email=email, age=age)
  
  return render_template("forms/wtf/user_info.html", form=user_info_form)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)