from flask import request, g
from functools import wraps

from .my_jwt import decode_token

def authenticated(func):
  @wraps(func)
  def token_verification(*args, **kwargs):
    token = None
    if "Authorization" in request.headers:
      try:
        typ, token = request.headers["Authorization"].split()

        if typ != "Bearer":
           raise ValueError
      except ValueError:
        return {"error": "Invalid token format, must be: Bearer <token>"}, 401
    else:
      return {"error": 'Authorization key not present in header'}, 401
    
    if token == None:
      return {"error": "token is missing"}

    try:
      g.user_id = decode_token(token)
    except ValueError as e:
      return {"error": str(e)}, 401

    return func(*args, **kwargs)
  return token_verification