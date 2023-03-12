from bs4 import BeautifulSoup as bs
import requests
import dateparser
import time
from .models import Resource

def get_page(url: str):
    r = requests.get(url)
    soup = bs(r.text, features="html.parser")
    return soup


def parse_scientific_ru(link):
    html = get_page(link + '/news')
    div = html.find('div', {'class': 'announce-list with-image super-wide single-column'})
    divs = div.find_all('div', {'class': 'list-item'})
    news_list = []
    for i in divs:
        href = i.find('div', {'class': 'announce'}).find('a').get('href')
        page = get_page(link + href)
        title = page.find('h1', {'itemprop': 'name headline'}).text.strip()
        date_text = page.find('article', {'class': 'article'}).find('div',{'class', 'prop time'})
        not_date = dateparser.parse(date_text.text)
        nd_date = time.mktime(not_date.timetuple())

        article = page.find('div', {'class': 'article-text'})
        contents = article.find_all('p')
        texts = []
        for content in contents:
            texts.append(content.text)
        news_content = ''.join(texts)

        news =  {
            'name': 'Scientific_ru',
            'link': link + href,
            'title': title,
            'nd_date': nd_date,
            'not_date': not_date,
            'content': news_content,
            'resource_id': Resource.objects.get(id=1)
        }
        news_list.append(news)
    return news_list

