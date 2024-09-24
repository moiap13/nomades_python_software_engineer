import jwt
from datetime import datetime, timedelta

SECRET_KEY = "super_secret"
ALGIRITHM = "HS256"

def create_token(user_id: str, days=7) -> str:
  """
  Function that issues a JWT token for a user

  Args:
    user_id (str): The id of the user
    days (int, optional): The number of days the token will be valid. Defaults to 7

  Returns:
    str: The JWT token as string
  """
  payload = {
    "sub": user_id,
    "iat": datetime.now().timestamp(),
    "exp": (datetime.now() + timedelta(days=days)).timestamp()
  }
  return jwt.encode(payload, SECRET_KEY, algorithm=ALGIRITHM)

def decode_token(token: str) -> str:
  """
  Function that decodes a JWT token and returns the user id

  Args:
    token (str): The JWT token to decode

  Returns:
    str: The user id stored inside the "sub" key of the payload
  """
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGIRITHM])
    return payload["sub"]
  except jwt.ExpiredSignatureError:
    raise Exception("Token Expired")
  except jwt.InvalidSignatureError:
    raise Exception("Invalid Token")
  