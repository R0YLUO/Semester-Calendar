from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewCalendarForm
from app.models import User 
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app.calendar import SemCalendar

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Main Page')

@app.route('/calendar', methods=['GET', 'POST'])
@login_required
def calendar():
    if current_user.has_calendar: 
        return render_template('calendar.html', title='Calendar')
    calendar_form = NewCalendarForm()
    if calendar_form.validate_on_submit(): 
        user_calendar = SemCalendar(calendar_form.start_date, calendar_form.end_date, 
                                 calendar_form.break_start, calendar_form.break_end)
        
    return render_template('new_calendar.html', title='Create calendar', form=calendar_form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data): 
            flash('Invalid username of password') 
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('calendar')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, has_calendar=False)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
