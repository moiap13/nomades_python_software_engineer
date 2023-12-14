from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from common import authenticated
#from common.forms import Login, SignUp, AddPost, SearchForm
import os
import csv
import firebase_admin
from firebase_admin import credentials, firestore

CURR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURR_DIR, "static/data")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

cred = credentials.Certificate(f"{CURR_DIR}/static/firebase_cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
print(db)

@app.route('/')
def index():
  return render_template("index.html")

##################################### DB PART ##################################
# ADD PART
@app.route("/add_user")
def add_user():
  created_at, d = db.collection(u"users2").add({
    "firstname": "Antonio",
    "lastname": "Pisanello",
    "age": 28,
    "hobbies": ["programming", "coding", "cinema"]
  })
  return f"Document created with id {d.id} at {created_at}"

@app.route("/add_user_set")
def add_user_set():
  created_at = db.collection(u"users").document(u"2piC0yD4ZVAStMiYKexx").set({
    "firstname": "Antonio",
    "lastname": "Pisanello",
    "hobbies": ["sport", "coding", "cinema"]
  })
  return f"Document created at {created_at}"

# READ PART
@app.route("/get_user")
def get_user():
  d = db.collection(u"users").document("2piC0yD4ZVAStMiYKexx").get()
  print(d.to_dict()["hobbies"][2])
  return f"Document getted successfully"

@app.route("/get_user/<id>")
def get_user_param(id):
  d = db.collection(u"users").document(id).get()
  print(d.to_dict())
  return f"Document getted successfully"

@app.route("/get_users")
def get_users():
  users = db.collection(u"users").stream()
  ret = {}
  for user in users:
    ret[user.id] = user.to_dict()
  return jsonify(ret)

# UPDATE PART
@app.route("/update_user/<id>")
def update_user_param(id):
  d = db.collection(u"users").document(id).update({
    "measures": {
      "height": 180,
      "weight": 100
    },
    "age": 30
  })
  print(d)
  return f"Document updated successfully"

@app.route("/update_user_set/<id>")
def update_user_set_param(id):
  d = db.collection(u"users").document(id).set({
    "height": 180,
    "age": 30
  })
  print(d)
  return f"Document updated successfully"

# DELETE PART
@app.route("/delete_user/<id>")
def delete_user_param(id):
  d = db.collection(u"users").document(id).delete()
  print(d)
  return f"Document deleted successfully"

# WHERE PART
@app.route("/get_user_age/<int:age>")
def get_user_age(age):
  stream = db.collection(u"users").where("age", "<", age).stream()
  ret = [{d.id: d.to_dict()} for d in stream]
  return jsonify(ret)

@app.route("/get_user_hobbies/<hobby>")
def get_user_hobbies(hobby):
  stream = db.collection(u"users").where("hobbies", "array_contains", hobby).stream()
  ret = [{d.id: d.to_dict()} for d in stream]
  return jsonify(ret)

@app.route("/get_user_in/")
def get_user_in():
  stream = db.collection(u"users").where("firstname", "in", ["antonio", "Elena"]).stream()
  ret = [{d.id: d.to_dict()} for d in stream]
  return jsonify(ret)

@app.route("/get_user_tricky/")
def get_user_tricky():
  stream = db.collection(u"users")\
    .where("firstname", "in", ["antonio", "Elena"])\
    .where("hobbies", "array_contains", "sport").stream()
  ret = [{d.id: d.to_dict()} for d in stream]
  return jsonify(ret)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)