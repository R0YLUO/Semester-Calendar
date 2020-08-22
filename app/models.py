from app import db
from datetime import datetime 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    calendar = db.relationship('SemesterCalendar', lazy='dynamic')

    def __repr__(self): 
        return 'User {}'.format(self.username)

class SemesterCalendar(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    start_date = db.Column(db.DateTime, default=datetime.utcnow())
    end_date = db.Column(db.DateTime, default=datetime.utcnow())
    weeks = db.relationship('Week', lazy='dynamic')

class Week(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    week_name = db.Column(db.String(64))
    list_of_todos = db.relationship('ToDoItem', lazy='dynamic')

class ToDoItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(128))

