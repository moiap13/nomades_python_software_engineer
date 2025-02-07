from functools import wraps

from flask import session, flash, redirect, url_for

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not session.get("loggedin", False):
      flash("Please login first", "danger")
      return redirect(url_for("login.login"))
    return func(*args, **kwargs)
  return inner