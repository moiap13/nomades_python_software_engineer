import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, request, render_template, session
from firebase_admin.firestore import DocumentReference

from forms.posts import PostCreateForm
from config.firestore_db import db

CURR_DIR: str = os.path.dirname(__file__)
ROOT_DIR: str = os.path.dirname(CURR_DIR)

posts_bp = Blueprint("posts", __name__, url_prefix="/posts")

@posts_bp.route("/add", methods=["GET", "POST"])
def add_post():
  create_post_form = PostCreateForm(request.form)

  if request.method == "POST" and create_post_form.validate():
    title: str = ...  # TODO: get title value from form
    body: str = ...   # TODO: get body value from form

    user_firestore_document_id: str = session["user"]["id"]
    user_firestore_docuemnt_reference: DocumentReference = db.collection(u"users").document(user_firestore_document_id)

    created_at = firestore.SERVER_TIMESTAMP

    # TODO: Create post object (dictionnary)
      # TODO: authors: list[DocumentReference]
      # TODO: title: str
      # TODO: body: str
      # TODO: created_at: timestamp

    # TODO: Add new post in the collection "posts" in Firestore
    # TODO: flash for "successfully inserted post" with category "success"
    # TODO: redirect to posts.list_posts

  return render_template('posts/create_post.html', form=create_post_form)

@posts_bp.route("/list", methods=["GET"])
def list_posts():
  # TODO: Get all posts from Firestore where the authors is myself
  # Don't forget the user's document id is stored in the session inside the key "user['id']"
  posts: list[dict[str, str]] = [] # list of dictionary where each dictionnary represent a post
  return render_template('posts/list_posts.html', posts=posts)