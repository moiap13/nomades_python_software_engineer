from flask import Blueprint, render_template, redirect, url_for, session, flash

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/info")
def user_info():
  if not session.get("loggedin", False):
    flash("Please log in first", "danger")
    return redirect(url_for("login.login"))
  
  return render_template(
    "users/user_info.html", 
    user=session["user"]
  )
