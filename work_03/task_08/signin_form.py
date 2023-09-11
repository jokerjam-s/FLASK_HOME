from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

_PASSWORD_MIN_LENGTH = 8


class SignInForm(FlaskForm):
    user_name = StringField('Имя пользователя', validators=[DataRequired()])
    user_email = EmailField('E-Mail', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=_PASSWORD_MIN_LENGTH)])
    confirm_password = PasswordField('Подтвердите пароль',
                                     validators=[DataRequired(),
                                     EqualTo('password', 'Пароль и подтверждение не совпадают!')])
    birth_day = DateField('Дата рождения', validators=[DataRequired()])
    agreement = BooleanField('Согласие на обработку данных')
