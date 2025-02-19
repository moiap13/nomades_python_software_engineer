from functools import wraps

from flask import session, flash, redirect, url_for

def authenticated(func):
  @wraps(func)
  def check_login(*args, **kwargs):
    if not session.get("loggedin", False):
      flash("Please login first", "warning")
      return redirect(url_for('login.login'))
    
    return func(*args, **kwargs)

  return check_login