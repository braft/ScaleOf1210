from wtforms import StringField, Form, validators, DataRequired

class InputForm(Form):
    inquiry = StringField(validators=[DataRequired()])
    submit = SubmitField('Inquire')
