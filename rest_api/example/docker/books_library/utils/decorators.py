from flask import request, jsonify, g
from functools import wraps

from .my_jwt import decode_token

def authenticated(func):
  @wraps(func)
  def token_verification(*args, **kwargs):
    token = None
    if 'Authorization' in request.headers:
      try:
        typ, token = request.headers["Authorization"].split()
        if typ != "Bearer":
          raise ValueError
      except ValueError:
        return {"error": "Invalid token format, must be: Bearer <token>"}, 401
        
    
    if token == None:
      return {"error": "Token is missing"}, 401


    try:
      g.user_id = decode_token(token)
    except Exception as e:
      return jsonify({"error", str(e)}), 401

    return func(*args, **kwargs)
  
  return token_verification