import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super secret"
ALGORITHM = "HS256"

def issue_token(user_id: str) -> str:
  payload = {
    "sub": user_id,
    "iat": datetime.utcnow().timestamp(),
    "exp": (datetime.utcnow() + timedelta(days=7)).timestamp()
  }
  return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token) -> str:
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload["sub"]
  except jwt.ExpiredSignatureError:
    raise Exception("Token expired")
  except jwt.InvalidSignatureError:
    raise Exception("Invalid token")
