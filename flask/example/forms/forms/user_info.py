from wtforms import Form, StringField, PasswordField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

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

class UserInfo(Form):
  firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=20)])
  lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=20)])
  email = EmailField('Email', validators=[DataRequired(), Email("Please enter a valid email address")])
  age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=12, max=99)], default=13)
  password = PasswordField('Password', validators=[DataRequired(), validate_password])
  gender = SelectField("Gender", choices=[(0, "Male"), (1, "female")], validators=[DataRequired()])
  submit = SubmitField('Submit')


