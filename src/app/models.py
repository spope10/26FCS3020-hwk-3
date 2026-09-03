'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student:
Description: Homework 03 - Model for the User Authentication Web App
'''

from app import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    passwd = db.Column(db.LargeBinary)
