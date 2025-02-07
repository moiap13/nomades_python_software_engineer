import sys, os
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOADS_DIR = os.path.join(PROJECT_DIR, "static", "uploads")
sys.path.append(PROJECT_DIR)

from flask import Blueprint, render_template, session

from helpers.decorators import authenticated

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/info")
@authenticated
def user_info():
  return render_template(
    "users/user_info.html",
    user=session.get("user", {})
  )
