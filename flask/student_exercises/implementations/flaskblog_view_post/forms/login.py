from wtforms import Form, StringField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, Email, NumberRange, EqualTo
from wtforms.fields.html5 import EmailField, IntegerField

def validate_password(form, field):
  if not any(char.isdigit() for char in field.data):
    raise ValueError("Password should contain at least one digit")
  
  if not any(char.isupper() for char in field.data):
    raise ValueError("Password should contain at least one uppercase character")
  
  if not any(char.islower() for char in field.data):
    raise ValueError("Password should contain at least one lowercase character")
  
  if not any(char in "!@#$%^.&*()-+" for char in field.data):
    raise ValueError("Password should contain at least one special character")


class RegisterForm(Form):
  firstname = StringField("Firstname", validators=[DataRequired(message="This field is MANDATORY"), Length(min=2, max=20)])
  lastname = StringField("Lastname", validators=[DataRequired(message="Cette donnée est obligatoire"), Length(min=2, max=40)])
  uid = StringField("Username", validators=[DataRequired(), Length(min=2, max=10)])
  email = EmailField("Email", validators=[DataRequired(), Email()])
  age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=13)])
  profile_picture = FileField("Profile Picture", validators=[DataRequired()])
  pwd = PasswordField("Password", validators=[DataRequired(), Length(min=8), validate_password])
  pwd2 = PasswordField("Retype Password", validators=[DataRequired(), EqualTo("pwd")])

class LoginForm(Form):
  uid_email = StringField("UID or Email", validators=[DataRequired()])
  pwd = PasswordField("Password", validators=[DataRequired()])
