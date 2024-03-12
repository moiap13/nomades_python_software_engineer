from flask import Flask, flash, render_template, request, session, redirect, url_for, jsonify
from python.forms import Register, ModifyUser, FormArticle
import hashlib
from functools import wraps
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.secret_key = "secret"

cred = credentials.Certificate("./static/flaskweek.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def authenticated(func):
  @wraps(func)
  def inner(*args, **kwargs):
    if not ("logged" in session and session["logged"]): # -> je ne suis pas loggé
      return redirect(url_for('login'))
    
    return func(*args, **kwargs)
  return inner

@app.route("/")
def index():
  return render_template("index.html")

# ======================= Login Part =======================

@app.route("/login", methods=["GET", "POST"])
def login():
  if 'logged' in session and session['logged']: # -> je suis deja loggé
    return redirect(url_for('userinfo'))
  
  if request.method == "POST":
    uid:str = request.form["tbx_uid"]
    pwd:str = request.form["tbx_pwd"]
    hpwd:str = hashlib.sha256(pwd.encode('utf-8')).hexdigest()

    user_ref = db\
                .collection(u"users")\
                .where("uid", "==", uid)\
                .where("pwd", "==", hpwd)\
                .stream()
                
    # assert user_ref contains only one or zero documents
    try:          
      user_reff = next(user_ref)
    except StopIteration:
      # Login failed
      return render_template("login/login.html", page="login", error="uid or pwd is false")

    session["user_id"] = user_reff.id
    session["logged"] = True
    return redirect(url_for("userinfo"))
  
  # GET part
  return render_template("login/login.html", page="login", error="")

@app.route("/register", methods=["GET", "POST"])
def register():
  if ("logged" in session and session["logged"]): # -> je suis loggé
    return redirect(url_for('userinfo'))
  
  regForm = Register(request.form)

  if request.method == "POST" and regForm.validate():
    # assert le formulaire est ok
    fn:str = regForm.firstname.data
    ln:str = regForm.lastname.data
    mail:str = regForm.email.data
    age:int = int(regForm.age.data)
    uid:str = regForm.uid.data
    pwd:str = regForm.password.data
    hpwd:str = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    
    user_exist = db.collection(u"users").where("uid", "==", uid).stream()

    try:
      next(user_exist)
    except StopIteration:
      # assert the uid is free
      pass
    else: # next didn't raise -> a user already have the uid
      # assert a user already have the uid
      flash("This user id is already used")
      return render_template('login/registerWTF.html', form=regForm, page="register")
    
    user = {
      u"firstname": fn,
      u"lastname": ln,
      u"mail": mail,
      u"age": age,
      u"uid": uid,
      u"pwd": hpwd
    }

    _, d = db.collection(u"users").add(user)
    session["logged"] = True
    session["user_id"] = d.id
    
    return redirect(url_for("secret"))
          
  return render_template('login/registerWTF.html', form=regForm, page="register")

@app.route("/logout")
@authenticated
def logout():
  session.clear()
  return redirect(url_for('index'))

# ======================= Users Part =======================

@app.route("/userinfo")
@authenticated
def userinfo():
  id = session["user_id"]
  mForm = ModifyUser(request.form)

  user = db.collection(u"users").document(id).get()
  assert(user.exists)

  print(user.to_dict())
  return render_template("users/user_info.html", form=mForm, id_user=id, user=user.to_dict())

@app.route("/user/<id_user>", methods=["POST", "GET"])
@authenticated
def user_methods(id_user):
  mFrom = ModifyUser(request.form)

  if request.method == "POST" and mFrom.validate():
    # assert le formulaire est ok
    fn:str = mFrom.firstname.data
    ln:str = mFrom.lastname.data
    mail:str = mFrom.email.data
    age:int = int(mFrom.age.data)
    uid:str = mFrom.uid.data
    
    user = {
      u"firstname": fn,
      u"lastname": ln,
      u"mail": mail,
      u"age": age,
      u"uid": uid
    }
    
    db.collection(u"users").document(id_user).update(user)
    return redirect(url_for('userinfo'))

  if request.method == "GET":
    db.collection(u"users").document(id_user).delete()
    return redirect(url_for('logout'))


  return redirect(url_for('userinfo'))

# ======================= Secret Part =======================

@app.route("/secret_sombre")
@authenticated
def secret():
  return "Secret part"

@app.route("/secret2")
@authenticated
def secret2():
  return "secret encore"

# ======================= Post Part =======================

@app.route('/post_article',methods=['POST','GET'])
@authenticated
def post():
    form=FormArticle(request.form)
    if request.method =='POST' and form.validate():
        t=form.titre.data
        c=form.corps.data
        #TODO: Insert post into post collections
        post = {
           u"titre": t,
           u"corps": c,
           u"user_id": session["user_id"]
        }

        db.collection(u"posts").add(post)
        return redirect(url_for('myposts'))
    return render_template('posts/post.html',form=form)

@app.route('/myposts')
@authenticated
def myposts():
    posts = {}
    # TODO: Get all the posts from the connected user (uid)
    user_id = session["user_id"]
    posts_db = db.collection("posts").where("user_id", "==", user_id).stream()
    
    for post in posts_db:
      posts[post.id] = post.to_dict()

    return render_template("posts/myposts.html", posts=posts)

@app.route('/delete_post/<string:id>', methods=['POST'])
@authenticated
def delete_post(id):
    #TODO: Delete the post with id in the posts collection
    p = db.collection(u"posts").document(id).delete()
    return redirect(url_for('myposts'))

@app.route('/post/<string:id>/')
def postview(id):
    #TODO: Get post with id = id
    p = db.collection(u"posts").document(id).get().to_dict()
    uid = db.collection(u"users").document(p["user_id"]).get().to_dict()["uid"]
    p["uid"] = uid
    return render_template('posts/postview.html',post=p)

if __name__ == '__main__':
  print("Crecction for firestore posts")
  app.run(debug=True, port=5050, host="0.0.0.0")