import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, render_template, redirect, url_for, session, flash

from utils.decorators import authenticated

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/info")
@authenticated
def user_info():
  return render_template(
    "users/user_info.html", 
    user=session["user"]
  )
