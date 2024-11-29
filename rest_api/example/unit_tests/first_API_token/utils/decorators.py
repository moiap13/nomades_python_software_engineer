from functools import wraps
from flask import request, g

from .my_jwt import decode_token

def authenticate(f):
  @wraps(f)
  def inner_func(*args, **kwargs):
    token = None
    # TODO: Check that the 'Authorization' key is part of the headers of the request
    if 'Authorization' not in request.headers:
      return {"message": 'no authorization key in headers'}, 401
    # TODO: check that the string for the key Authorization starts with Bearer
    # TODO: get the token (the token follows the Bearer keyword after a space)
    try:
      bearer, token = request.headers.get("Authorization").split(" ")
      assert bearer == "Bearer"
    except (ValueError, AssertionError):
      return {"message": 'Authorization is not on the form "Bearer <TOKEN>"'}, 401

    # if not bearer.startswith("Bearer "):
    #   return {"message": 'Authorization is not on the form "Bearer <TOKEN>"'}, 401
    
    # token: str = bearer.split(" ")[1]
    
    # TODO: use my_jwt.decode_token function to authenticate the user
    try:
      user_id: str = decode_token(token)
    except Exception:
      return {"message": 'Token is not more valid, please create a new one'}, 401
    
    g.user_id = user_id
    return f(*args, **kwargs)
  
  return inner_func
