from flask import Blueprint, request
import requests
from bs4 import BeautifulSoup

parser = Blueprint('parser', __name__)

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'ru-RU,en;q=0.8',
    'upgrade-insecure-requests': '1',
    # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
index = 0


def get_html(url, params=None):
    """
    Фунция которая посылает GET запрос на ресурс и получает html страницу
    :param url: Url адрес страницы для парсинга
    :param params: Параметры запроса
    :return: Возвращает объект Response библиотеки requests
    """
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    """
    Функция для получения общего кол-ва страниц, которые нужно паарсить.
    Эти данные парсяться из пагинатора.
    :param html: Принимает html страницу
    :return: Возвращает int (число), которое указывает на кол-во страниц
    """
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='j-pgn-page')

    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1


def get_content(html):
    """
    Функция которая парсит необходимый мне контент (информацию по заказам из биржи Freelance.ua)
    :param html: Принимает html страницу
    :return: Возвращает результат парсинга, список словарей. Где в каждом словаре информация об одном заказе.
    """
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='j-order')
    result = []
    global index
    for item in items:
        index = index + 1

        price = item.find('div', class_='flex-price-tag').find_next('span').get_text(strip=True)
        if price == 'По договоренности':
            price_result = 0
        else:
            price_result = price

        if item.find('i', class_='fa-clock-o'):
            published = item.find('i', class_='fa-clock-o').find_parent().get_text(strip=True)
        else:
            published = 'Дата публикации не указана.'

        if item.find('i', class_='fa-map-marker'):
            city = item.find('i', class_='fa fa-map-marker').find_parent().get_text(strip=True)
        else:
            city = 'Город не указан'

        if item.find('i', class_='fa-comments-o'):
            offers = item.find('i', class_='fa-comments-o').find_parent().get_text(strip=True)
            offers_int = [int(s) for s in offers.split() if s.isdigit()]
            result_offers = offers_int[0]
        else:
            result_offers = 0

        if item.find('i', class_='fa-calendar'):
            active = item.find('i', class_='fa-calendar').find_parent().get_text(strip=True)
        else:
            active = 'Дедлайн приема заявок не указан.'

        if item.find('span', class_='pro'):
            pro = True
        else:
            pro = False

        if item.find('i', class_='fa-briefcase'):
            work_type = item.find('i', class_='fa-briefcase').find_parent().get_text(strip=True)
        elif item.find('i', class_='fa-anchor'):
            work_type = item.find('i', class_='fa-anchor').find_parent().get_text(strip=True)
        else:
            work_type = None

        result.append({
            'id': index,
            'title': item.find('header', class_='l-project-title').get_text(strip=True),
            'description': item.find('article', class_='').get_text(strip=True),
            'link': item.find('header', class_='l-project-title').find_next('a').get('href'),
            'city': city,
            'price': price_result,
            'published': published,
            'work_type': work_type,
            'active_to': active,
            'offers': result_offers,
            'pro': pro
        })
    return result


def parse(cat, pg):
    """
    Основная ф-ия парсинга данных. Тут происходит основная работа.
    :param cat: Принимает транслитерацию категории. Этот параметр передается в URL
    :param pg: Кол-во страниц которые нужно спарсить
    :return: Возвращает словарь со всеми данными.
    """
    url = f"https://freelance.ua/orders/?orders={cat}"
    html = get_html(url)
    if html.status_code == 200:
        orders = []
        paginate = get_pages_count(html.text)

        if pg >= paginate:
            parsing_page_count = paginate + 1
        else:
            parsing_page_count = paginate - paginate + pg + 1

        for page in range(1, parsing_page_count):
            print(f'Парсинг страницы {page} из {pg} ...')
            html = get_html(url, params={'page': page, 'pc': 1})
            orders.extend(get_content(html.text))
        # print(f'Спаршено {len(orders)} заказов.')
        return {'result': orders, 'total': len(orders), 'page_total': parsing_page_count-1}
    else:
        # print('Ошибка запроса!')
        return {'error': 'Request Error. Status code not 200!'}


@parser.route('/freelance_ua', methods=['POST'])
def profile():
    global index
    index = 0
    req_info = request.get_json()
    return parse(req_info['category'], req_info['page'])
