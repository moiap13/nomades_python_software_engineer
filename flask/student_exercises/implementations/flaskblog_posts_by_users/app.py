import os

from flask import Flask, render_template

from blueprints.login import login_bp
from blueprints.user import user_bp
from blueprints.posts import posts_bp

CURR_DIR: str = os.path.dirname(__file__)
CSV_FILE: str = os.path.join(CURR_DIR, "users.csv")
UPLOADS_DIR: str = os.path.join(CURR_DIR, "static", "uploads")

app = Flask(__name__, template_folder="src")
app.config["SECRET_KEY"] = "secret"

@app.route("/")
def index():
  return render_template("index.html")

app.register_blueprint(login_bp)
app.register_blueprint(user_bp)
app.register_blueprint(posts_bp)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8081)