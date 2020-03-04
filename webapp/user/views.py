from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/registration")
def registration():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title_reg = "Регистрация"
    reg_form = RegistrationForm()
    return render_template("user/registration.html", title_reg=title_reg,
                           reg_form=reg_form)


@blueprint.route('/process-registration', methods=['POST'])
def process_registration():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        new_user = User(username=reg_form.username.data,
                        email=reg_form.email.data, role='user')
        new_user.set_password(reg_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались, зайдите под своим именем.')
        return redirect(url_for('user.login'))
    else:
        for field, errors in reg_form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле '{getattr(reg_form, field).label.text}': - {error}")
        return redirect(url_for('user.registration'))
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('user.registration'))


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title_auth = "Авторизация"
    login_form = LoginForm()
    return render_template("user/login.html", title_auth=title_auth,
                           login_form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'С возвращением, {user}')
            return redirect(url_for('news.index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет, админ'
    else:
        return 'Ты не админ!'


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('news.index'))
