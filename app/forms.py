from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    level = IntegerField('Level', validators=[DataRequired(), NumberRange(min=0,max=5)])
    submit = SubmitField('Submit')