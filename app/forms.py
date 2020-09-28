from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Post author',validators=[Required()])
    content = TextAreaField('Post content', validators=[Required()])
    submit = SubmitField('Submit')