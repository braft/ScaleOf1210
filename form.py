from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired

class InputForm(Form):
    inquiry = StringField(validators=[DataRequired()])
    submit = SubmitField('Inquire')
