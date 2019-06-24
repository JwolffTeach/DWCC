from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class BuilderForm(FlaskForm):
    """ hero """
    heroname = StringField('Name', validators=[DataRequired()])
    heroclass = SelectField('Class', choices=[('', ''), ('Bard', 'Bard'), ('Cleric', 'Cleric'), ('Druid', 'Druid'), ('Fighter', 'Fighter'), ('Paladin', 'Paladin'), ('Ranger', 'Ranger'), ('Thief', 'Thief'), ('Wizard', 'Wizard')])
    herorace = StringField('Race', validators=[DataRequired()])
    heroalignment = StringField('Alignment', validators=[DataRequired()])

    """ looks """
    heroeyes = StringField('Eyes', validators=[DataRequired()])
    herohair = StringField('Hair', validators=[DataRequired()])
    heroclothing = StringField('Clothing', validators=[DataRequired()])
    herobody = StringField('Body', validators=[DataRequired()])
    heroskin = StringField('Skin', validators=[DataRequired()])
    herosymbol = StringField('Symbol', validators=[DataRequired()])

    submit = SubmitField('Create Character')


class LooksForm(FlaskForm):
    eyes = SelectField('eyes', choices=[[]])
    hair = SelectField('hair', choices=[[]])
    clothing = SelectField('clothing', choices=[[]])
    body = SelectField('body', choices=[[]])
    skin = SelectField('skin', choices=[[]])
    symbol = SelectField('symbol', choices=[[]])

    submit = SubmitField('Add Looks')