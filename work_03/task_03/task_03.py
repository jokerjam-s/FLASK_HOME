import random as rnd

from flask import Flask, render_template
from work_03.task_03.data_model import db, Student, Rating

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.cli.command('db-init')
def db_init():
    db.create_all()
    print("Create database - Ok")


@app.cli.command('fill-db')
def fill_db():
    for i in range(1, 6):
        new_student = Student(first_name=f'Student {i}', second_name=f'Student {i}', group_name=f'GR-1')
        db.session.add(new_student)

    for i in range(1, 4):
        for j in range(1, 5):
            new_rate = Rating(student_id=j, subject=f'Subject {i}', rating=rnd.randint(3, 5))
            db.session.add(new_rate)

    db.session.commit()


@app.route("/")
@app.route("/index/")
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run(debug=True)