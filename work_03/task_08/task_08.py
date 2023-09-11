from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from work_03.task_08.data_model import db, User
from work_03.task_08.signin_form import SignInForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user_data.db"
app.config['SECRET_KEY'] = '9737b994-63b0-4151-bf13-5c6c6e16725b'
db.init_app(app)
csrf = CSRFProtect(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Create database - Ok')


@app.errorhandler(404)
def error_404(err):
    return 'Resource not found! ', 404


@app.route('/')
@app.route('/index/')
def index():
    """Главная страница"""
    return render_template('main.html')


@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    """Регистрация нового пользователя в системе"""
    sign_form = SignInForm()
    if request.method == 'POST' and sign_form.validate():
        new_user = User(
            user_name=sign_form.user_name.data,
            user_email=sign_form.user_email.data,
            birth_day=sign_form.birth_day.data,
            password=generate_password_hash(sign_form.password.data),
            agreement=sign_form.agreement.data
        )
        db.session.add(new_user)
        db.session.commit()
        print(new_user.id)

        return redirect(url_for('sign_result', id=new_user.id))

    return render_template('signin.html', form=sign_form)


@app.route('/sign-result/<int:id>')
def sign_result(id):
    """Резульаь регистрации пользователя"""
    user = User.query.filter_by(id=id)
    if user is None:
        flash('Ошибка регистрации!', 'error')
    else:
        flash('Пользователь зарегистрирован!', 'ok')
    return render_template('sign_result.html')
