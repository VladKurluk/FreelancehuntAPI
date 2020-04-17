'''
API ендпоинты для передачи данных полученых с Фрилансхант API в приложение Vue.js
'''

from flask import Blueprint
from freelance_api.api_call import *

api = Blueprint('api', __name__)

@api.route('/curent_profile')
def profile():
    return get_profile()

@api.route('/freelancers')
def freelancers_list():
    return get_freelancers()

@api.route('/my_feed')
def feed_list():
    return get_my_feed()