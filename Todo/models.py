# models.py
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):# 사용자 모델 정의
    id = db.c


class Todo(db.Model): #To-do 모델 정의
    id = db.Column(db.Integer, primary_key=True)
    