from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()],
                           render_kw={"class": "form-control",
                           "placeholder": "Введите имя пользователя"}
                           )
    password = PasswordField("Пароль", validators=[DataRequired()],
                             render_kw={"class": "form-control",
                             "placeholder": "Введите пароль"}
                             )
    remember_me = BooleanField('Запомнить меня', render_kw={
                                "class": "form-check-input"
                                }
                               )
    submit = SubmitField('Войти', render_kw={
                             "class": "btn btn-success btn-lg btn-block"
                             }
                         )
