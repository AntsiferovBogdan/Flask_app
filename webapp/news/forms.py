from flask_wtf import FlaskForm
from webapp.news.models import News
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class CommentForm(FlaskForm):
    news_id = HiddenField('ID новости', validators=[DataRequired()])
    comment_text = StringField('Комментарий',
                               validators=[DataRequired()],
                               render_kw={"class": "form-control",
                                          "placeholder": "Оставьте свой комментарий"
                                          }
                               )
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary",
                                                 "background-color": "#f0db80;"
                                                 })

    def validate_news_id(self, news_id):
        if not News.query.get(news_id.data):
            raise ValidationError('Новость отсутствует')
