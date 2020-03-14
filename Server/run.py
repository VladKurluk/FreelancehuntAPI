'''
Точка входа в приложение. 
Из пакета freelance_api импортируеться экземпляр Flask приложения, и запускаеться.
'''

from freelance_api import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()