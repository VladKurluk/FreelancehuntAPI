'''
API ендпоинты для передачи данных полученых с Фрилансхант API в приложение Vue.js
'''

from flask import Blueprint
from freelance_api.api_call import get_profile

api = Blueprint('api', __name__)

@api.route('/curent_profile')
def profile():
    res = get_profile()
    return res