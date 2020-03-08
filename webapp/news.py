from bs4 import BeautifulSoup
from datetime import datetime


def get_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%b. %d, %Y')
            except(ValueError):
                published = datetime.now()
            save_news(title, url, published)
    return False
