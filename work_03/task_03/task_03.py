import random as rnd

from flask import Flask, render_template
from work_03.task_03.data_model import db, Student, Rating

"""Набор для генерации тестовых данных"""
_FIRST_NAMES = ('Иван', 'Петр', 'Сергей', 'Николай', 'Тимофей')
_SECOND_NAME = ('Сидоров', 'Петров', 'Тимофеев', 'Сергеев', 'Николаев')
_GROUPS = ('ГР-1', 'ПР-2', 'ТМ-1', 'МО-3')
_SUBJECT = ('Математика', 'Физика', 'Химия', 'Физкультура', 'Информатика')

"""Инициализация приложения"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.cli.command('db-init')
def db_init():
    """Подготовка базы данных"""
    db.create_all()
    print('Create database - Ok')


@app.cli.command('fill-db')
def fill_db():
    """Заполнение тестовыми данными"""
    for i in range(1, 6):
        new_student = Student(first_name=rnd.choice(_FIRST_NAMES), second_name=rnd.choice(_SECOND_NAME),
                              group_name=rnd.choice(_GROUPS))
        db.session.add(new_student)

    for i in range(1, 6):
        for j in range(len(_SUBJECT)):
            new_rate = Rating(student_id=i, subject=_SUBJECT[j], rating=rnd.randint(3, 5))
            db.session.add(new_rate)

    db.session.commit()
    print('Test data generation - Ok')


@app.route("/")
@app.route("/index/")
def index():
    students = Student.query.all()
    context = {
        "students": students
    }
    return render_template('main.html', **context)


@app.errorhandler(404)
def page_404(err):
    return 'Error 404. Page not found!', 404


if __name__ == '__main__':
    app.run(debug=True)
