from flask import Blueprint
import requests
from bs4 import BeautifulSoup

parser = Blueprint('parser', __name__)


# URL = 'https://auto.ria.com/newauto/marka-opel/'
HOST = 'https://auto.ria.com'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'accept': '*/*'}

CARS = []


def get_html(url, params=None):
    """
    Фунция которая получает в ответ на запрос html страницу
    :param url: Url
    :param params: Параметры запроса
    :return: Возвращает объект Response библиотеки requests
    """
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='mhide')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')

    cars = []
    for item in items:
        uan_price = item.find('span', class_='grey size13')
        if uan_price:
            uan_price = uan_price.get_text(strip=True).replace('•', '')
        else:
            uan_price = 'Цена в гривне не указана!'

        CARS.append({
            'title': item.find('h3', class_='proposition_name').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'city': item.find('svg', class_='svg-i16_pin').find_next('strong').get_text(strip=True),
            'usd_price': item.find('span', class_='green').get_text(strip=True),
            'uan_price': uan_price
        })
    return CARS


def parse():
    # marka_auto = input('Введите марку авто, для подстаговки в URL https://auto.ria.com/newauto/marka-..... \n')
    # url = f'https://auto.ria.com/newauto/marka-{marka_auto.lower()}/'
    url = "https://auto.ria.com/newauto/marka-opel/"
    html = get_html(url)
    if html.status_code == 200:
        cars = []

        paginate = get_pages_count(html.text)

        for page in range(1, paginate + 1):
            print(f'Парсинг страницы {page} из {paginate} ...')
            html = get_html(url, params={'page': page})
            cars.extend(get_content(html.text))
        print(f'Спаршено {len(cars)} автомобилей.')
    else:
        print('Ошибка запроса!')





@parser.route('/')
def profile():
    parse()
    return {'Hello': CARS}