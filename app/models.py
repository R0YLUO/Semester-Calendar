from app import db
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    password_hash = db.Column(db.String(128))
    calendars = db.relationship('Calendar', back_populates='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)

class Calendar(db.Model): 
    __tablename__ = 'calendars'
    id = db.Column(db.Integer, primary_key=True) 
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    break_start = db.Column(db.DateTime())
    break_end = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='calendars')
    weeks = db.relationship('Week', back_populates='calendar', lazy=True)

    def create_weeks(self): 
        delta_first_half = self.break_start - self.start_date
        weeks_first_half = delta_first_half.days // 7

        delta_break = self.break_end - self.break_start
        weeks_break = delta_break.days // 7 + 1

        delta_second_half = self.end_date - self.break_end
        weeks_second_half = delta_second_half.days // 7 

        for week_num in range(1, weeks_first_half + 1): 
            week = Week(week_name="Week "+str(week_num), calendar_id=self.id) 
            db.session.add(week)

        for break_num in range(1, weeks_break + 1): 
            break_week = Week(week_name="Break Week "+str(break_num), calendar_id=self.id)
            db.session.add(break_week)
    
        for week_num in range(weeks_first_half + 1, weeks_first_half + weeks_second_half + 1): 
            week = Week(week_name="Week "+str(week_num), calendar_id=self.id)
            db.session.add(week) 
        db.session.commit() 

class Week(db.Model): 
    __tablename__ = 'weeks'
    id = db.Column(db.Integer, primary_key=True) 
    week_name = db.Column(db.String(64))
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendars.id'))
    calendar = db.relationship('Calendar', back_populates='weeks')
    todoitems = db.relationship('ToDoItem', back_populates='week', lazy=True)

class ToDoItem(db.Model): 
    __tablename__ = 'todoitems'
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(128))
    week_id = db.Column(db.Integer, db.ForeignKey('weeks.id'))
    week = db.relationship('Week', back_populates='todoitems')
