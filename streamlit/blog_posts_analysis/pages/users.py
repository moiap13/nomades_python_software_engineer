import streamlit as st
import pandas as pd
import plotly.express as px

from config.firestore_db import db

def fetch_authors():
  authors_ref = db.collection("users")  # Adjust collection name if needed
  authors = authors_ref.stream()
  data = []
  for author in authors:
      author_dict = author.to_dict()
      age = author_dict.get("age")
      author_id = author.id
      data.append({"author_id": author_id, "age": age})
  return pd.DataFrame(data)

def author_analysis():
  st.subheader("Author Age Analysis")
      
  # Fetch authors' data
  author_df = fetch_authors()

  # Display age statistics
  st.write("### Author Age Statistics")
  mean_age = author_df["age"].mean()
  std_age = author_df["age"].std()
  st.write(f"Mean Age: {mean_age:.2f}")
  st.write(f"Standard Deviation of Age: {std_age:.2f}")

  # Categorize age into groups
  age_bins = [0, 18, 30, 40, 50, 60, 100]
  age_labels = ["<18", "18-30", "31-40", "41-50", "51-60", "60+"]
  author_df["age_group"] = pd.cut(author_df["age"], bins=age_bins, labels=age_labels, right=False)

  # Display age group distribution
  st.write("### Age Group Distribution")
  age_group_counts = author_df["age_group"].value_counts().sort_index()
  st.write(age_group_counts)

  # Plot the age group distribution as a bar chart
  age_group_chart = px.bar(age_group_counts, x=age_group_counts.index, y=age_group_counts.values, 
                            title="Number of Authors in Each Age Group", labels={"x": "Age Group", "y": "Count"})
  st.plotly_chart(age_group_chart)

  # Plot histogram of author ages
  st.write("### Histogram of Author Ages")
  age_histogram = px.histogram(author_df, x="age", nbins=20, title="Distribution of Author Ages")
  st.plotly_chart(age_histogram)

  # Plot boxplot of author ages
  st.write("### Boxplot of Author Ages")
  age_boxplot = px.box(author_df, y="age", title="Boxplot of Author Ages")
  st.plotly_chart(age_boxplot)

st.set_page_config(page_title="Authors Analysis", layout="wide")

st.title("Authors Analysis")
author_analysis()