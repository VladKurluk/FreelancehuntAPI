"""
Файл запуска приложения.
Из ф-ла application.py импортиться ф-ция, которая создает приложение create_app
"""

from application import create_app

app = create_app('development')

if __name__ == '__main__':
    app.run()