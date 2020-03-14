'''
Здесь находяться функции обращения к Фрилансхант API для получения данных.
'''

from freelance_api.token import token
import requests

REQUEST_HEADER = {
    'Authorization': token
}

def get_profile():
    url = "https://api.freelancehunt.com/v2/my/profile"
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Ошибка обращения к API'}