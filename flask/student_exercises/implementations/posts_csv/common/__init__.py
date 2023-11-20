from flask import session, redirect, url_for
from functools import wraps

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("logged" in session and session["logged"]):
      return redirect(url_for('login'))
    
    assert session["logged"]
    return func(*args, **kwargs)
  return inner