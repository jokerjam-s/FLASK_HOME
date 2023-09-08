"""Модель данных Студенты-Оценки. Задание 3"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    """Модель таблицы данным студент"""
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    group_name = db.Column(db.String(20), nullable=False)
    student_email = db.Column(db.String(250))
    ratings = db.relationship('Rating', backref='student', lazy=False)

    def __str__(self):
        return f'{self.first_name} {self.second_name}, группа {self.group_name}'

    def __repr__(self):
        return f'Student({self.first_name},{self.second_name},{self.group_name})'


class Rating(db.Model):
    """Модель таблицы данных оценки"""
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    subject = db.Column(db.String(150), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return f'{self.subject} - {self.rating}'

    def __repr__(self):
        return f'Rating({self.subject}, {self.rating}, {self.student_id})'



