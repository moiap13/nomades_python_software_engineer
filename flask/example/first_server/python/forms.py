from wtforms import Form, validators, StringField, PasswordField, EmailField, IntegerField

class Login(Form):
  email = EmailField('Email', [validators.input_required(), validators.email()])
  password = PasswordField('Password', [validators.input_required()])

class SignUp(Form):
  firstname = StringField('Enter Firstname', [validators.input_required(), validators.length(2, 10)])
  lastname = StringField('Lastname', [validators.input_required(), validators.length(2, 10)])
  email = EmailField('Email', [validators.input_required(), validators.email()])
  age = IntegerField("Age", [validators.NumberRange(13, 20)])
  uid = StringField("User-Id", [validators.input_required(), validators.length(3, 5, "le user id doit être compris entre 3 et 5 charactères")])
  password = PasswordField('Password', [validators.data_required(), validators.equal_to('confirm',message='PASSWORDS DONT MATCH')])
  confirm = PasswordField('Confirm password')