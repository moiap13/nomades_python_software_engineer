import os
from flask import Flask, render_template, request
import uuid

app = Flask(__name__)

CURR_DIR: str = os.path.dirname(__file__)
UPLOAD_DIR: str = os.path.join(CURR_DIR, "uploads")

@app.route("/")
def index():
  return render_template("index.html")

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
def files():
  if request.method == "POST":
    files = request.files.getlist("fileInput")
    for file in files:
      if file.content_type.split("/")[0] == "image":
        print(file.content_type)
        ext: str = file.filename.split(".")[-1]
        file_path: str = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.{ext}")
        file.save(file_path)
    return f"File successfully saved id {file_path}"

  return render_template("forms/sending_files.html") 

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)