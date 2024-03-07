
from wtforms import Form, EmailField, PasswordField, StringField
from wtforms.validators import email, DataRequired, equal_to

class LoginForm(Form):
  email = EmailField('Email address', validators=[email("Rentre un email valide"), DataRequired()])
  pwd = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
  email = EmailField('Email address', validators=[email(), DataRequired()])
  pwd = PasswordField('Password', validators=[DataRequired()])
  pwd_confirm = PasswordField('Confirm password', validators=[equal_to(pwd)])

# class Register(Form):
#     firstname = StringField('Enter Firstname', [validators.input_required(), validators.length(2, 10)])
#     lastname = StringField('Lastname', [validators.input_required(), validators.length(2, 10)])
#     email = StringField('Email', [validators.input_required(), validators.email()])
#     age = IntegerField("Age")
#     uid = StringField("User-Id", [validators.input_required(), validators.length(3, 5, "uid must be between 3 and 5 chars")])
#     password = PasswordField('Password', [validators.data_required(), validators.equal_to('confirm',message='PASSWORDS DONT MATCH')])
#     confirm = PasswordField('Confirm password')

# class Login(Form):
#     uid = StringField("User Id", [validators.input_required()])
#     password = PasswordField('Password', [validators.data_required()])

