<<<<<<< HEAD
from flask import Blueprint, render_template
from webapp.user.decorators import admin_required
=======
from flask import Blueprint
from flask_login import current_user, login_required
>>>>>>> 1808b33d73b001eab03e0a84b723da347964977d

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
<<<<<<< HEAD
@admin_required
def admin_index():
    title = 'Панель управления'
    return render_template('admin/index.html',
                           page_title=title)
=======
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет, админ'
    else:
        return 'Ты не админ!'
>>>>>>> 1808b33d73b001eab03e0a84b723da347964977d
