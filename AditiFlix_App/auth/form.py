from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL, ValidationError)

from password_validator import PasswordValidator

class PasswordValid:
    def __init__(self, message=None):
        if not message:
            message = u'Your password must be at least 8 characters, and contain an upper case letter, \
            a lower case letter and a digit'
        self.message = message

    def __call__(self, form, field):
        schema = PasswordValidator()
        schema \
            .min(8) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits()
        if not schema.validate(field.data):
            raise ValidationError(self.message)


class SignupForm(FlaskForm):
    """Sign up for a user account."""
    username = StringField('Username', [
        DataRequired(message='Your username is required'),
        Length(min=4, message='Your username is too short')])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
        EqualTo("confirmPassword", message='Passwords must match.'),
        PasswordValid()
    ])
    confirmPassword = PasswordField('Retype Password')
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Prove you are human. Try again")])
    submit = SubmitField('Submit')

class SigninForm(FlaskForm):
    """Sign up for a user account."""
    username = StringField('Username', [
        DataRequired(message='Your username is required')
    ])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password.")
    ])
    submit = SubmitField('Submit')
