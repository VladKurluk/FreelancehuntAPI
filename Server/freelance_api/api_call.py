"""
Здесь находяться функции обращения к Фрилансхант API для получения данных.
"""

from os import environ
import requests

'''
Токен для доступа к Фрилансхант API
'''
FREELANCEHUNT_API_KEY = environ.get('FREELANCEHUNT_API_KEY')


REQUEST_HEADER = {
    'Authorization': 'Bearer ' + str(FREELANCEHUNT_API_KEY)
}

PROFILE_URL = "https://api.freelancehunt.com/v2/my/profile"
FEED_URL = "https://api.freelancehunt.com/v2/my/feed"
SKILLS_URL = "https://api.freelancehunt.com/v2/skills"

def get_profile():
    url = PROFILE_URL
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
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

def get_skills():
    url = SKILLS_URL
    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

def get_freelancers():
    url = f"https://api.freelancehunt.com/v2/freelancers?filter[skill_id]={124}"

    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Ошибка обращения к API'}

def get_freelancers_by_params(params):
    url = f"https://api.freelancehunt.com/v2/freelancers?filter[skill_id]={params['id']}&page[number]={params['page']}"

    payload = {}
    headers = REQUEST_HEADER
    response = requests.request("GET", url, headers=headers, data = payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Ошибка обращения к API'}
