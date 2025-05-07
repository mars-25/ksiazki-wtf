from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField("Tytuł zadania", validators=[DataRequired()])
    description = TextAreaField("Opis", validators=[DataRequired()])
    completed = BooleanField("Ukończone")
    submit = SubmitField("Zapisz")
