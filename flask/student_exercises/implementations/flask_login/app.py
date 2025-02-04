import os
import csv
import hashlib

from flask import Flask, render_template, request

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    # TODO: get tbx values (uid, pwd)
    # TODO insert user in CSV file
      # TODO: open csv file in 'a' mode, for inserting
      # TODO: insert the user in the format uid,pwd
      # TODO: at the end display the message user "successfully inserted"
      # TODO: If any error (uid already existing, or mis validation) -> display the correct error
      
      # TODO: Bonus, hash the password
      # TODO: Bonus, add repeat password input and check matching
      pass
  else:
    return render_template('login/register.html')

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    # TODO: get tbx values (uid, pwd)
    # TODO read user in CSV file
      # TODO: open csv file in 'r' mode
      # TODO: check if form.uid exists in csv file
        # TODO: if yes -> check if the password for this uid in csv file match form.pwd
          # TODO: If yes -> return "Login Successfull"
      # TODO: otw -> return "Invalid credentials"
      # TODO: Bonus, hash the password 
    pass
  else:  
    return render_template("login/login.html")
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)