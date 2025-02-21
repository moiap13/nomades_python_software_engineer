import os, sys
ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)

import jwt
from datetime import datetime, timedelta

from dotenv import dotenv_values

envs = dotenv_values('/etc/secrets/.env')

SECRET_KEY: str = envs["JWT_SECRET"]
ALG: str = envs["JWT_ALG"]

def create_token(user_id: str, days=7) -> str:
  payload: dict[str, str | float] = {
    "sub": user_id,
    "iat": datetime.now().timestamp(),
    "exp": (datetime.now() + timedelta(days=days)).timestamp()
  }
  return jwt.encode(payload, SECRET_KEY, ALG)

def decode_token(token: str) -> str:
  try:
    payload: dict[str, str | float] = jwt.decode(token, SECRET_KEY, [ALG])
    return payload["sub"]
  except jwt.ExpiredSignatureError:
    raise ValueError("Token Expired")
  except jwt.InvalidSignatureError:
    raise ValueError("Invalid Token")
