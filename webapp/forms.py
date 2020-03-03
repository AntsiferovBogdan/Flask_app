from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
    submit = SubmitField('Войти', render_kw={
                             "class": "btn btn-success btn-lg btn-block"
                             }
                         )
