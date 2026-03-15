from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddMovieForm(FlaskForm):
    name = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')