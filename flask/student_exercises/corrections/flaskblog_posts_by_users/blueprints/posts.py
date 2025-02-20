import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Blueprint, request, render_template, session, flash, redirect, url_for, jsonify
from firebase_admin.firestore import DocumentSnapshot, DocumentReference, SERVER_TIMESTAMP
from firebase_admin import firestore

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

from forms.posts import PostCreateForm
from config.firestore_db import db
from utils.decorators import authenticated

CURR_DIR: str = os.path.dirname(__file__)
ROOT_DIR: str = os.path.dirname(CURR_DIR)
CHARTS_DIR: str = os.path.join(ROOT_DIR, "static", "imgs", "charts")

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

  post_data: dict[str, str | list[DocumentReference] | float] = db.collection(u"posts").document(post_id).get().to_dict()
  authors_str: list[str] = []

  for author_ref in post_data["authors"]:
    author_data: dict[str, str | int] = author_ref.get().to_dict()
    fullname: str = f"{author_data['firstname'].capitalize()} {author_data['lastname'].capitalize()}"
    authors_str.append(fullname)

  post_data["authors"] = authors_str
  post: dict[str, str | list[str], float] = post_data.copy()

  return render_template('posts/view_post.html', post=post)

@posts_bp.route("/analyse")
@authenticated
def analyse_posts():
  posts = db.collection(u"random_posts").get()
  
  data = []
  for post in posts:
    post_dict: dict[str, str | list[DocumentReference]] = post.to_dict()
    created_at = post_dict.get("created_at")
    authors = post_dict.get("authors", [])

    for author in authors:
      author_data = author.get().to_dict()
      data.append({
        "created_at": created_at,
        "author": f"{author_data['firstname']} {author_data['lastname']}"
      })
  
  df = pd.DataFrame(data)
  df["created_at"] = pd.to_datetime(df["created_at"])
  df["date"] = df["created_at"].dt.date

  post_counts = df.groupby("date").size().reset_index(name="post_counts")

  post_counts_users =  df.groupby(["date", "author"]).size().reset_index(name="post_counts")

  post_ratio = (df.groupby("author").size() / len(df.created_at.unique())).sort_index().reset_index(name="ratio")

  line_chart = px.line(post_counts, x="date", y="post_counts", title="Post created by Date (Line chart)")
  bar_chart = px.bar(post_counts, x="date", y="post_counts", title="Post created by Date (Bar chart)")

  bar_chart_users = px.bar(
    post_counts_users,
    x="date",
    y="post_counts",
    color="author",
    title="Post per users (Bar chart)",
    barmode="group",
  )

  pie_chart_users = px.pie(
    post_ratio,
    names="author",
    values="ratio",
    title="post ratio per user",
    labels={"author": "User full name", "ratio": "Percentage"},
    color="author"
  )

  table_html = df.to_html(classes="table table-striped table-hover", justify="left")
  
  return render_template(
    'posts/post_analysis.html',
    line_chart=line_chart.to_html(full_html=False),
    bar_chart=bar_chart.to_html(full_html=False),
    bar_chart_users=bar_chart_users.to_html(full_html=False),
    pie_chart_users=pie_chart_users.to_html(full_html=False),
    pandas_html=table_html
  )