import streamlit as st

def main():
  st.set_page_config(page_title="Dashboard", layout="wide")
  st.title("Welcome to the analysis dashboard")
  st.markdown("Choose an analysis")
  st.page_link("pages/posts.py", label="Post Analysis")
  st.page_link("pages/users.py", label="Post Analysis")

if __name__ == '__main__':
  main()
