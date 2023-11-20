from flask import Flask, render_template, request, session, redirect, url_for
from common import authenticated
from common.forms import Login, SignUp, AddPost, SearchForm
import os
#TODO: add firestore imports
import firebase_admin
from firebase_admin import credentials, firestore
import hashlib
import random
import string
import uuid

CURR_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(CURR_DIR, "static/data")
UPLOAD_DIR = os.path.join(CURR_DIR, "static/imgs/uploads")

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.secret_key = "secret"

#TODO: create firestore instance (connection with credentials and instatiation of db object)
cred = credentials.Certificate(f"{CURR_DIR}/static/cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/userinfo")
@authenticated
def user_info():
  d = db.collection(u"users").document(session["id"]).get()
  d = d.to_dict()
  return render_template("users/userinfo.html", email=d["email"], pwd=d["pwd"], uid=d["uid"])
    
@app.route("/login", methods=["GET", "POST"])
def login():
  if "logged" in session and session["logged"]:
    return redirect(url_for('user_info'))
  
  login_form = Login(request.form)

  if request.method == "POST" and login_form.validate():
    #TODO: Login using firebase documents instead of csv files
    email:str = login_form.email.data
    pwd:str = login_form.password.data
    
    try:
      d = next(db.collection(u"users").where("email", "==", email).stream())
    except StopIteration:
      return "Invalid email"
    
    pwd = hashlib.sha256((pwd+d.to_dict()["salt"]).encode("utf-8")).hexdigest()
    if d.to_dict()["pwd"] == pwd:
      session["id"] = d.id
      session["logged"] = True
      return redirect(url_for("user_info"))
    return "Ivalid password"
  return render_template("login/login.html", form=login_form)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if "logged" in session and session["logged"]:
      return redirect(url_for('user_info'))
  
  signup_form = SignUp(request.form)

  if request.method == "POST" and signup_form.validate():
    fn = signup_form.firstname.data
    ln = signup_form.lastname.data
    email = signup_form.email.data
    age = signup_form.age.data
    uid = signup_form.uid.data
    pwd = signup_form.password.data
    salt = "".join([random.choice(string.ascii_letters) for _ in range(10)])
    pwd = pwd + salt
    hpwd = hashlib.sha256(pwd.encode("utf-8")).hexdigest()

    user = {
      "firstname": fn,
      "lastname": ln,
      "email": email,
      "age": age,
      "uid": uid,
      "pwd": hpwd,
      "salt": salt
    }

    if db.collection(u"users").where("email", "==", email).count().get()[0][0].value > 0:
    #if len(db.collection(u"users").where("email", "==", email).get()) > 0: # -> Equivalent to the above line
      return "Email already used"

    _, d = db.collection(u"users").add(user)
    session["id"] = d.id
    session["logged"] = True
    return redirect(url_for("user_info"))
  return render_template("login/signup.html", form=signup_form)
@app.route("/logout")
def logout():
  session.clear()
  return redirect(url_for('index'))

# TODO: Post things: view_post, view_posts and create_post using the firestore database.

@app.route("/add_post", methods=["POST", "GET"])
@authenticated
def add_post():
  add_post_form = AddPost()

  if request.method == "POST":
    title:str = add_post_form.title.data
    content:str = add_post_form.content.data
    categories:str = add_post_form.categories.data

    image_extension:str = add_post_form.image.data.filename.split(".")[-1]
    image_name:str = str(uuid.uuid4()) + "." + image_extension
    image_path:str = os.path.join(UPLOAD_DIR, image_name)
    add_post_form.image.data.save(image_path)

    author:str = db.collection(u"users").document(session["id"]).get().to_dict()["uid"]
    id_user:str = session["id"]

    db.collection(u"posts").add({
      "title": title,
      "content": content,
      "categories": categories,
      "author": author,
      "id_docuument_user": id_user,
      "image_name": image_name
    })

    return redirect(url_for("view_posts"))
  return render_template("posts/add_post.html", form=add_post_form)

@app.route("/view_posts")
def view_posts():
  posts = db.collection(u"posts").stream()
  final_posts = []
  for post in posts:
    pd = post.to_dict()
    if "title" in pd and "author" in pd:
      pd["post_id"] = post.id
      final_posts.append(pd)
  return render_template("posts/view_posts.html", posts=final_posts)

@app.route("/view_post/<post_id>")
def view_post(post_id):
  post = db.collection(u"posts").document(post_id).get()
  pd = post.to_dict()
  pd["post_id"] = post_id
  return render_template("posts/view_post.html", post=pd)

# TODO: Perform the search on post using the attributes: title, content and categories in the firestore database
@app.route("/search")
def search():
  search_form = SearchForm(request.form)
  final_posts = []

  if request.method == "POST" and search_form.validate():
    keyword:str = search_form.search.data

    cat_posts = db.collection(u"posts").where("categories", "")


  return render_template("search/search.html", form=search_form, posts=final_posts)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port="8080", debug=True)