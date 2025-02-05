from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

def validate_password(form, field):
  if len(field.data) < 8:
    raise ValueError("Password should be at least 8 characters long")
  
  if not any(char.isdigit() for char in field.data):
    raise ValueError("Password should contain at least one digit")
  
  if not any(char.isupper() for char in field.data):
    raise ValueError("Password should contain at least one uppercase character")
  
  if not any(char.islower() for char in field.data):
    raise ValueError("Password should contain at least one lowercase character")
  
  if not any(char in "!@#$%^&*()-+" for char in field.data):
    raise ValueError("Password should contain at least one special character")

class Register(Form):
  uid = StringField("User ID", validators=[DataRequired(), Length(min=3, max=10)])
  pwd = PasswordField("Password", validators=[DataRequired()])
  pwd2 = PasswordField("Retype Password", validators=[DataRequired(), EqualTo("pwd")])


class Login(Form):
  uid = StringField("User ID", validators=[DataRequired()])
  pwd = PasswordField("Password", validators=[DataRequired()])

