from flask import request, jsonify, g
from functools import wraps

from .my_jwt import decode_token

def authenticated(func):
  @wraps(func)
  def token_verification(*args, **kwargs):
    #TODO: Implement token verification
    return func(*args, **kwargs)
  
  return token_verification