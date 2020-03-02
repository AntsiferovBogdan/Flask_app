from flask import Flask, render_template
from webapp.news import get_news
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        page_title = 'Daily Bugle'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = get_news()
        return render_template('index.html', page_title=page_title,
                               weather=weather, news=news)
    return app
