from wtforms import Form, validators, StringField, PasswordField, IntegerField, TextAreaField

class Register(Form):
    firstname = StringField('Enter Firstname', [validators.input_required(), validators.length(2, 10)])
    lastname = StringField('Lastname', [validators.input_required(), validators.length(2, 10)])
    email = StringField('Email', [validators.input_required(), validators.email()])
    age = IntegerField("Age")
    uid = StringField("User-Id", [validators.input_required(), validators.length(3, 5, "le user id doit être compris entre 3 et 5 charactères")])
    password = PasswordField('Password', [validators.data_required(), validators.equal_to('confirm',message='PASSWORDS DONT MATCH')])
    confirm = PasswordField('Confirm password')

class Login(Form):
    uid = StringField("User Id", [validators.input_required()])
    password = PasswordField('Password', [validators.data_required()])

class ModifyUser(Form):
    firstname = StringField('Enter Firstname', [validators.input_required(), validators.length(2, 10)])
    lastname = StringField('Lastname', [validators.input_required(), validators.length(2, 10)])
    email = StringField('Email', [validators.input_required(), validators.email()])
    age = IntegerField("Age")
    uid = StringField("User-Id", [validators.input_required(), validators.length(3, 5, "le user id doit être compris entre 3 et 5 charactères")])

class FormArticle(Form):
    titre=StringField('Titre',[validators.length(min=2,max=200)])
    corps=TextAreaField('Message',[validators.length(min=2,max=200)])