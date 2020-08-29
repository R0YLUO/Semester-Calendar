from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User
from datetime import datetime, date, time, timezone

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None: 
            raise ValidationError('Please use a different username.')

class NewCalendarForm(FlaskForm): 
    start_date = DateField("Semester start date", validators=[DataRequired()])
    end_date = DateField("Semeter end date", validators=[DataRequired()])
    break_start = DateField("Mid-semester break start date", validators=[DataRequired()])
    break_end = DateField("Mid-semester break end date", validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_start_date(self, start_date): 
        if start_date.data.weekday() != 0: 
            raise ValidationError("Starting date for semester should be a Monday.")

    def validate_end_date(self, end_date): 
        if end_date.data.weekday() != 4:  
            raise ValidationError("Ending date for semester should be a Friday.")
        if end_date.data <= self.start_date.data: 
            raise ValidationError("Semester end date is earlier than semester start date")
    
    def validate_break_start(self, break_start): 
        if break_start.data.weekday() != 0: 
            raise ValidationError("Starting date for mid-semester break should be a Monday.")
        if not (self.start_date.data < break_start.data < self.end_date.data): 
            raise ValidationError("Semester break should be within the semester period.")

    def validate_break_end(self, break_end): 
        if break_end.data.weekday() != 4: 
            raise ValidationError("Ending date for mid-semester break should be a Friday.")
        if break_end.data <= self.break_start.data: 
            raise ValidationError("Break end date should be after break start date.")
        if break_end.data >= self.end_date.data: 
            raise ValidationError("Semester break should be within the semester period.")