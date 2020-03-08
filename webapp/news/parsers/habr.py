from bs4 import BeautifulSoup
from webapp import db
from webapp.news.models import News
from webapp.news.parsers.utils import date_translate, get_html, save_news


def get_news_snippets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order_by=date")
    if html:
        soup = BeautifulSoup(html, "html.parser")
        all_news = soup.find("ul", class_="content-list_posts").find_all("li", class_="content-list__item_post")
        for news in all_news:
            title = news.find("a", class_="post__title_link").text
            url = news.find("a", class_="post__title_link")["href"]
            published = news.find("span", class_="post__time").text
            published = date_translate(published)
            save_news(title, url, published)
    return False


def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            news_text = soup.find('div',
                                  class_='post__text-html').decode_contents()
            if news_text:
                news.text = news_text
                db.session.add(news)
                db.session.commit()
