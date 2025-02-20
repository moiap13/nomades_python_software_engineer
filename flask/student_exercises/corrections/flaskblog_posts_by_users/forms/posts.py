from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostCreateForm(Form):
  title = StringField("Post Title", validators=[DataRequired(), Length(1, 99)])
  body = TextAreaField("Post Body", validators=[DataRequired()])