from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.fields.core import SelectField
from wtforms.validators import Email, Required

class CommentForm(FlaskForm):
    comment = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    category_choices = ['Tech', 'Life', 'Food', 'Culture']
    title = StringField('Title',validators=[Required()])
    category = SelectField('Category', choices = category_choices, validators = [Required()])
    content = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(), Email(message="Not a valid email address")])
    submit = SubmitField('Subscibe')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')








