from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
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
    herorace = SelectField('Race', coerce=int)
    heroalignment = SelectField('Alignment', coerce=int)

    """ looks """
    heroeyes = SelectField('eyes', coerce=int, validators=[Optional()])
    herohair = SelectField('hair', coerce=int, validators=[Optional()])
    heroclothing = SelectField('clothing', coerce=int, validators=[Optional()])
    herobody = SelectField('body', coerce=int, validators=[Optional()])
    heroskin = SelectField('skin', coerce=int, validators=[Optional()])
    herosymbol = SelectField('symbol', coerce=int, validators=[Optional()])

    """ stats """
    herostrength = IntegerField('Strength')
    herodexterity = IntegerField('Dexterity')
    heroconstitution = IntegerField('Constitution')
    herointelligence = IntegerField('Intelligence')
    herowisdom = IntegerField('Wisdom')
    herocharisma = IntegerField('Charisma')

    """ hp of stats """
    herohp = IntegerField('HP')

    submit = SubmitField('Create Character')


class BasicMoveForm(FlaskForm):
    movename = StringField('Move Name', validators=[DataRequired()])
    movedescription = PageDownField('Move Description', validators=[DataRequired()])
    movedetails = PageDownField('Move Details', validators=[DataRequired()])

    submit = SubmitField('Add Move')