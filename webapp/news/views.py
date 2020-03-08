from flask import abort, Blueprint, current_app, render_template
from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    title = "Новости"
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title,
                           weather=weather, news_list=news_list
                           )


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    chosen_news = News.query.filter(News.id == news_id).first()
    if not chosen_news:
        abort(404)

    return render_template('news/single_news.html',
                           page_title=chosen_news.title,
                           chosen_news=chosen_news
                           )
