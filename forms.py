from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class TodoForm(FlaskForm):
    title = StringField("Tytuł książki", validators=[DataRequired()])
    author = StringField("Autor", validators=[DataRequired()])
    bookgenere = StringField("Gatunek", validators=[DataRequired()])
    description = TextAreaField("Opis", validators=[DataRequired()])
    bookrating = IntegerField("Ocena", validators=[DataRequired(),NumberRange(min=1, max=10)])
    submit = SubmitField("Zapisz")
