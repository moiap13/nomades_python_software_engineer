import streamlit as st
import pandas as pd
import plotly.express as px

from config.firestore_db import db

def fetch_posts():
  posts = db.collection(u"random_posts").stream()

  data = []
  for post in posts:
    post_dict: dict = post.to_dict()
    created_at: "timestamp" = post_dict.get("created_at")
    authors: list = post_dict.get("authors")

    for author in authors:
      author_dict = author.get().to_dict()
      data.append({
        "created_at": created_at,
        "author": f"{author_dict['firstname']} {author_dict['lastname']}"
      })
  
  posts_df = pd.DataFrame(data)

  posts_df["created_at"] = pd.to_datetime(posts_df["created_at"])
  posts_df["date"] = posts_df["created_at"].dt.date

  return posts_df

def post_analysis():
  posts_df = fetch_posts()

  min_date = posts_df["date"].min()
  max_date = posts_df["date"].max()

  st.sidebar.header("Filters")
  selected_dates: tuple["timestamp"] = st.sidebar.date_input("Select dates", [min_date, max_date], min_value=min_date, max_value=max_date)

  authors_name = posts_df["author"].unique()
  selected_authors: list[str] = st.sidebar.multiselect("Select authors", options=authors_name, default=authors_name)

  filtered_df = posts_df.copy()
  try:
    filtered_df = posts_df[posts_df["date"].between(selected_dates[0], selected_dates[1])]
  except:
    st.error("Please select start date and end date")
    return
  
  filtered_df = filtered_df[filtered_df["author"].isin(selected_authors)]

  st.dataframe(filtered_df)

  posts_counts = filtered_df.groupby("date").size().reset_index(name="post_counts")
  posts_counts["cumulative_post_count"] = posts_counts["post_counts"].cumsum()

  posts_counts_authors = filtered_df.groupby(["date", "author"]).size().reset_index(name="post_counts")
  posts_counts_authors["cumulative_post_count"] = posts_counts_authors.groupby("author")["post_counts"].cumsum()

  author_post_counts = filtered_df.groupby("author").size().reset_index(name="total_posts")

  line_chart = px.line(posts_counts, x="date", y="post_counts", title="total post created by date")
  cumulative_line_chart = px.line(posts_counts, x="date", y="cumulative_post_count", title="Cumulative posts created")
  bar_chart = px.bar(posts_counts, x="date", y="post_counts", title="Number of post created per day")
  bar_chart_authors = px.bar(
    posts_counts_authors,
    x="date", y="post_counts",
    color="author",
    title="Post per author per day",
    barmode="group"
  )
  cumulative_by_user_chart = px.line(
    posts_counts_authors, 
    x="date", 
    y="cumulative_post_count", 
    color="author", 
    title="Cumulative Posts Created Per User (Line Chart)"
  )
  pie_chart = px.pie(
    author_post_counts, 
    names="author", 
    values="total_posts",
    title="Post Contribution Ratio Per Author",
  )

  st.plotly_chart(line_chart)
  st.plotly_chart(bar_chart)
  st.plotly_chart(cumulative_line_chart)
  st.plotly_chart(bar_chart_authors)
  st.plotly_chart(cumulative_by_user_chart)
  st.plotly_chart(pie_chart)

st.set_page_config(page_title="Post Analysis", layout="wide")

st.title("Post Analysis")
post_analysis()