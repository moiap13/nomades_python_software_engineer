from wtforms import Form, validators, StringField, PasswordField, EmailField, IntegerField, SelectMultipleField

def get_categories_from_csv() -> list[tuple[str, str]]:
  import os
  import csv

  CURR_DIR = os.path.dirname(os.path.abspath(__file__)).split("common")[0]
  DATA_DIR = os.path.join(CURR_DIR, "static/data")

  categories = []
  with open(f"{DATA_DIR}/categories.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    categories = [(row[1], row[1]) for row in reader]
  return categories

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

class AddPost(Form):
  categories = SelectMultipleField("Categories", choices=get_categories_from_csv(), validators=[validators.input_required()])

class SearchForm(Form):
  pass