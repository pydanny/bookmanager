"""
WTForms Documentation:    http://wtforms.simplecodes.com/
Flask WTForms Patterns:   http://flask.pocoo.org/docs/patterns/wtforms/
Flask-WTF Documentation:  http://packages.python.org/Flask-WTF/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import Form, SubmitField, TextField, PasswordField, Required

class SignInForm(Form):
    """Just a simple signin form."""
    username = TextField('Username', validators=[Required()])
    api_key = TextField('API Key', validators=[Required()])
