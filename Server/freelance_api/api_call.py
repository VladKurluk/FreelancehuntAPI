"""
Здесь находяться функции обращения к Фрилансхант API для получения данных.
"""

from freelance_api.token import token
import requests

REQUEST_HEADER = {
    'Authorization': token
}

PROFILE_URL = "https://api.freelancehunt.com/v2/my/profile"
FEED_URL = "https://api.freelancehunt.com/v2/my/feed"

def get_profile():
    url = PROFILE_URL
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.text.encode('utf8'))
        return {'error': 'Ошибка обращения к API'}

def get_my_feed():
    url = FEED_URL
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()


def get_freelancers():
    url = "https://api.freelancehunt.com/v2/freelancers?filter[skill_id]=124"
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Ошибка обращения к API'}
