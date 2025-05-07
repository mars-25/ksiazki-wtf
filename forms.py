from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField("Tytuł książki", validators=[DataRequired()])
    autor = StringField("Autor", validators=[DataRequired()])
    bookgenere = StringField("Gatunek", validators=[DataRequired()])
    description = TextAreaField("Opis", validators=[DataRequired()])
    completed = BooleanField("Czy przeczytana")
    submit = SubmitField("Zapisz")
