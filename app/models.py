from app import db
from datetime import datetime 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) 
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    calendar = db.relationship('Calendar')

    def __repr__(self): 
        return 'User {}'.format(self.username)

class Calendar(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    start_date = db.Column(db.DateTime, default=datetime.utcnow())
    end_date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weeks = db.relationship('Week')

class Week(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    week_name = db.Column(db.String(64))
    calendar_id = db.Column(db.Integer, db.ForeignKey('calendar.id'))
    list_of_todos = db.relationship('ToDoItem')

class ToDoItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    description = db.Column(db.String(128))
    week_id = db.Column(db.Integer, db.ForeignKey('week.id'))

