import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, render_template, redirect, url_for, session, flash
from firebase_admin.firestore import DocumentReference, DocumentSnapshot
from firebase_admin import firestore

from utils.decorators import authenticated
from config.firestore_db import db

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/info")
@authenticated
def user_info():
  return render_template(
    "users/user_info.html", 
    user=session["user"]
  )

@user_bp.route("/all")
def get_all_users():
  users = db.collection("users").stream()
  users_list: list[dict[str, str | int]] = []
  for user in users:
    user_data: dict[str, str | int] = user.to_dict()
    user_data["id"] = user.id
    users_list.append(user_data)
  
  return render_template('users/all_users.html', users=users_list)

@user_bp.route("/<user_id>/posts")
def get_posts_per_user(user_id: str):
  post_query: list[DocumentSnapshot] = db.collection(u"posts").where("authors", "array_contains", db.collection(u"users").document(user_id)).order_by("created_at", direction=firestore.Query.DESCENDING).get()
  # posts: list[dict[str, str | float | list[DocumentReference]]] = [{"title": post.to_dict()["title"], "body": post.to_dict()["body"], "id": post.id} for post in post_query] 
  # posts: list[dict[str, str | float | list[DocumentReference]]] = [{**post.to_dict(), "id": post.id} for post in post_query] 
  posts: list[dict[str, str | float | list[DocumentReference]]] = [post.to_dict() | {"id": post.id} for post in post_query]

  return render_template('posts/list_posts.html', posts=posts, public=True)