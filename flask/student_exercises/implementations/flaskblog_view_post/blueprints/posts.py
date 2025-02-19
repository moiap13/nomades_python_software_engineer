import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, request, render_template, session, flash, redirect, url_for
from firebase_admin.firestore import DocumentSnapshot, DocumentReference, SERVER_TIMESTAMP
from firebase_admin import firestore

from forms.posts import PostCreateForm
from config.firestore_db import db
from utils.decorators import authenticated

CURR_DIR: str = os.path.dirname(__file__)
ROOT_DIR: str = os.path.dirname(CURR_DIR)

posts_bp = Blueprint("posts", __name__, url_prefix="/posts")

@posts_bp.route("/add", methods=["GET", "POST"])
@authenticated
def add_post():
  create_post_form = PostCreateForm(request.form)

  if request.method == "POST" and create_post_form.validate():
    title: str = create_post_form.title.data
    body: str = create_post_form.body.data

    user_firestore_document_id: str = session["user"]["id"]
    user_firestore_docuemnt_reference: DocumentReference = db.collection(u"users").document(user_firestore_document_id)

    created_at = SERVER_TIMESTAMP
    
    post_data: dict[str, str | float | list[DocumentReference]] = {
      "title": title,
      "body": body,
      "created_at": created_at,
      "authors": [user_firestore_docuemnt_reference]
    }

    db.collection(u"posts").add(post_data)

    flash("Successfully inserted post", "success")
    return redirect(url_for("posts.list_posts"))

  return render_template('posts/create_post.html', form=create_post_form)

@posts_bp.route("/list", methods=["GET"])
@authenticated
def list_posts():
  user_firestore_docuemnt_reference: DocumentReference = db.collection(u"users").document(session["user"]["id"]) 
  posts_query: list[DocumentSnapshot] = db.collection(u"posts").where("authors", "array_contains", user_firestore_docuemnt_reference).order_by("created_at", direction=firestore.Query.DESCENDING).get()
  posts: list[dict[str, str | float | list[DocumentReference]]] = [] 

  for post in posts_query:
    post_dict: dict[str, str | float | list[DocumentReference]] = post.to_dict()
    post_dict["id"] = post.id
    posts.append(post_dict)

  return render_template('posts/list_posts.html', posts=posts)

@posts_bp.route("/delete/<post_id>")
@authenticated
def delete_post(post_id: str):
  post_ref: DocumentReference = db.collection(u"posts").document(post_id)
  post_snapshot: DocumentSnapshot = post_ref.get()
  if not post_snapshot.exists:
    flash(f"Post with id={post_id} doesn't exists in database", "danger")
    return redirect(url_for('posts.list_posts'))

  user_firestore_docuemnt_reference: DocumentReference = db.collection(u"users").document(session["user"]["id"])  
  if user_firestore_docuemnt_reference not in post_snapshot.to_dict()["authors"]:
    flash(f"User with id={session['user']['id']} is not authors of post with id={post_id}", "danger")
    return redirect(url_for('posts.list_posts')) 

  post_ref.delete()


  flash("Post successfully deleted", "success")
  return redirect(url_for('posts.list_posts'))

@posts_bp.route("/view/<post_id>")
@authenticated
def view_post(post_id: str):
  # TODO (optional): Check if user has right to view post

  # TODO: Get the post from firestore
  # TODO: get the full names of authors
  # TODO: create a dictionnary for the post
  post: dict[str, str | list[str], float] = {}
    # TODO: title: str
    # TODO: body: str
    # TODO: authors: list[str]
    # TODO: created_at: timestamp

  return render_template('posts/view_post', post=post)