from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class AddPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image Url', validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])

    submit = SubmitField('Publish Post')