import os

from flask import Flask, render_template
from dotenv import dotenv_values

from helpers.decorators import authenticated
from routes.login import login_bp
from routes.user import user_bp

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

app = Flask(__name__, static_folder="src")
app.config["SECRET_KEY"] = dotenv_values(os.path.join(CURR_DIR, ".env"))["SECRET_KEY"]

app.register_blueprint(login_bp)
app.register_blueprint(user_bp)

@app.route("/")
def index():
  return render_template("index.html")
 
@app.route("/protected")
@authenticated
def protected():
  return "Protected route"

@app.route("/private")
@authenticated
def private():
  return "private"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)