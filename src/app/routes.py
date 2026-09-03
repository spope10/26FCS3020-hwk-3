'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: 
Description: Homework 03 - Routes for the User Authentication Web App
'''

from app import app, db
from app.models import User
from app.forms import SignUpForm, LoginForm
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

# TODO #1: implement the sign-up functionality:
# * if passwords match, generate a "salted" hashed password using bcrypt
# * instantiate a user object from form information
# * store the user information in the database (hint: use db.session)
# * redirect to index
@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.passwd.data == form.passwd_confirm.data:
            return redirect(url_for('index'))

    return render_template('signup.html', form=form)
    
# TODO #2: implement the login functionality:
# * query the database for the user with given id 
# * if passwords match, complete the login procedure
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass

    return render_template('login.html', form=form)

# TODO #3: implement the sign-out functionality
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def list_users(): 
    users = User.query.all()
    return render_template('users.html', users=users)