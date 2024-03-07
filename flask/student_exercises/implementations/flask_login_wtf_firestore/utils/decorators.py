from flask import session, redirect, url_for
from functools import wraps

def authenticated(func):
  @wraps(func)
  def inner_func(*args, **kwargs):
    if not ("logged" in session and session["logged"]):
      return redirect(url_for("login"))
    return func(*args, **kwargs)
  
  return inner_func

def public(func):
  @wraps(func)
  def inner_func(*args, **kwargs):
    if 'logged' in session and session['logged']:
      return redirect(url_for('userinfo'))
    return func(*args, **kwargs)

  return inner_func