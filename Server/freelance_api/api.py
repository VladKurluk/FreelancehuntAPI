'''
API ендпоинты для передачи данных полученых с Фрилансхант API в приложение Vue.js
'''

from flask import Blueprint, request
from freelance_api.api_call import *

api = Blueprint('api', __name__)

@api.route('/curent_profile')
def profile():
    return get_profile()

@api.route('/my_feed')
def feed_list():
    return get_my_feed()

@api.route('/freelancers', methods=['GET', 'POST'])
def freelancers_list():
    if request.method == 'GET':
        return get_freelancers()
    elif request.method == 'POST':
        req_info = request.get_json()
        return get_freelancers_by_params(req_info)

@api.route('/skills')
def skills_list():
    return get_skills()