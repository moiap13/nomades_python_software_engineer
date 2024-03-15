from functools import wraps
from flask import request, jsonify, g

from .my_jwt import decode_token

def authenticated(func):
  @wraps(func)
  def inner_func(*args, **kwargs):
    token = None
    if 'Authorization' in request.headers:
      try:
        type, token = request.headers['Authorization'].split()
        if type.lower() != "bearer":
          raise ValueError
      except ValueError:
        return jsonify({'message': 'Invalid token format, must be: Bearer <token>'}), 401

    if not token:
      return jsonify({'message': 'Token is missing'}), 401
    
    try:
      g.user_id = decode_token(token)
    except Exception as e:
      return jsonify({'message': str(e)}), 401
    
    return func(*args, **kwargs)
  
  return inner_func

    
