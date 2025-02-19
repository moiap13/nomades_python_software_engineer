import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, render_template, redirect, url_for, session, flash
from firebase_admin.firestore import DocumentReference

from utils.decorators import authenticated

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
  # TODO: Get all the users of the database
  users = ... # TODO: define the type of users 
  return render_template('users/all_users.html', users=users)

@user_bp.route("/user/<user_id>/posts")
def get_posts_per_user(user_id: str):
  # TODO: Get all the posts for the given user
  posts: list[dict[str, str | float | list[DocumentReference]]] = [] 
  return render_template('posts/list_posts.html', posts=posts)