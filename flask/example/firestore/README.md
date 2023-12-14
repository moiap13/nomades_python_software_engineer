# FLASK WTF
## Description
This is a simple flask app that uses flask_wtf to create a form and validate it.
## Installation
```bash
conda install -c conda-forge flask-wtf
conda install -c conda-forge email-validator # For email validation
```
## Setup
You are provided a directory called `flask_wtf` that contains a flask server implementation in the `app.py` file. This server has already the login, signup and logout routes. Thehe `login` and `signup` forms, are available in the `forms.py` file located inside the `common` folder. Inside the `static` folder you'll find a directory called `data` that contains some csv files(`users.csv`, `categories.csv`, `posts.csv` and `post_categorys.csv`). You'll use these files to store the data.

## CSV Files
| File Name | Description |
| --- | --- |
| users.csv | Contains the user data |
| categories.csv | Contains the categories data |
| posts.csv | Contains the posts data |
| post_categorys.csv | Contains the link for the posts and their category data |

The `users.csv` and the `categories.csv` files contain some data. The `posts.csv` and the `post_categorys.csv` files doesn't have any data. **Your task is to populate these files and make some request on it**

## Your work

### 1. Create the forms
Inside the `forms.py` file you'll find the `Signup` and the `Login` classes. You'll need to **create** the `AddPost` class. The `AddPost` class should have the following fields:
- `title`, a `StringField`
- `content`, a `TextAreaField`
- `categories`, **Note: The `categories` field is a `SelectMultipleField` it allows us to select multiple values at once using the cmd key or control key** *This form field is already given in the `forms.py` file*

You should also **create** the `SearchForm` class. The `SearchForm` class should have the following fields:
- `search_value`, a `StringField`

### 2. Create the routes
Inside the `app.py` file you'll find the `login`, `signup` and `logout` routes. You'll need to **create** the following routes:
- `/add_post`, a `GET` and a `POST` route that will:
    - `GET`: render the `add_post.html` template
    - `POST`: validate the form and add the post data to the `posts.csv` file. *Think about that all the fields of the `posts.csv` are not all given by teh form*
- `/view_post/<post_id>`, a `GET` route that take the `post_id` as a parameter and will:
    - `GET`: render the `view_posts.html` template providing the given post as parameter to the template **(Template is already done for you)**
- `/view_posts`, a `GET` route that will:
    - `GET`: render the `view_posts.html` template providing all the posts as a list of posts(dict) and pass it as parameter to the template **(Template is already done for you)**
- `/search`, a GET route that will:
    - `GET`: render the `search.html` template
    - `POST`: validate the form and search for the post. Search for the posts mean: display a list of posts filtered by the search value. The search can be performed on the title, content or categories. *You'll need to use the `SearchForm` form*

*For the `view_post` and `view_posts` routes, please take a look on the templates files to see how the parameter will be used*

### 3. Create the templates
Inside the `templates` folder you'll find the `posts` and the `search` folder. Inside the `posts` folder you are mandated to create the `add_post.html`template. Inside the `search` folder you are mandated to create the `search.html` template. 

The `add_post` template should have the following fields:
- `title`, a `StringField`
- `content`, a `TextAreaField`
- `categories`, a `SelectMultipleField`
and send them by `POST` to the route `/add_post` this route should add the post data to the `posts.csv` file.

The `search` template should have the following fields:
- `search_value`, a `StringField`
and send them by `POST` to the route `/search` this route should search for the post and display a list of posts filtered by the search value. The search can be performed on the title, content or categories. **(OPTIONAL) If you want to go further on this exercise, try adding a click on the post to view it (use the `view_post` route)** 
