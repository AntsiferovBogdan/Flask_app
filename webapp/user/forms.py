from flask_wtf import FlaskForm
from webapp.user.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", [DataRequired()],
                           render_kw={"class": "form-control",
                           "placeholder": "Введите имя пользователя"}
                           )
    password = PasswordField("Пароль", [DataRequired()],
                             render_kw={"class": "form-control",
                             "placeholder": "Введите пароль"}
                             )
    remember_me = BooleanField("Запомнить меня", render_kw={
                            "class": "form-check-input"
                                }
                               )
    submit = SubmitField("Войти", render_kw={
                             "class": "btn btn-success btn-lg btn-block"
                             }
                         )


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", [DataRequired()],
                           render_kw={"class": "form-control",
                           "placeholder": "Придумайте имя пользователя"}
                           )
    email = StringField("Email", [DataRequired(), Email()],
                        render_kw={"class": "form-control",
                        "placeholder": "Введите адрес e-mail"}
                        )
    password = PasswordField("Пароль", [DataRequired()],
                             render_kw={"class": "form-control",
                             "placeholder": "Задайте пароль"}
                             )
    confirm = PasswordField([DataRequired(), EqualTo("password")],
                            render_kw={"class": "form-control",
                            "placeholder": "Повторите пароль"}
                            )
    submit = SubmitField("Зарегистрироваться", render_kw={
                             "class": "btn btn-success btn-lg btn-block"
                             }
                         )

    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).count()
        if users_count > 0:
            raise ValidationError('Данное имя пользователя уже занято.')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).count()
        if users_count > 0:
            raise ValidationError('Указанная почта уже зарегистрирована.')
