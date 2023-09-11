"""Модель данных пользователя"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Пользователь, объектная модель"""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    user_email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    birth_day = db.Column(db.Date, nullable=False)
    agreement = db.Column(db.Boolean, nullable=False)

    def __str__(self):
        return f'{self.user_name}, {self.user_email}'