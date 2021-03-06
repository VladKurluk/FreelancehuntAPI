## Приложение для работы с фриланс биржей Freelancehunt.com

**Основная цель:** Создать прложение которое будет включать в себя как [клиентскую часть](https://github.com/VladKurluk/FreelancehuntAPI/tree/master/Client) (в моем случае клиент - Vue SPA), так и [серверную часть](https://github.com/VladKurluk/FreelancehuntAPI/tree/master/Server) (Python/Flask).  
Бекенд будет получать данные из биржи [freelancehunt.com](https://freelancehunt.com/). Через предоставляемый биржой публичный API 2.0 и дальше отдавать полученные данные в JSON формате на клиент.

**Дополнительные задачи:**

-   Создать модуль для парсинга других бирж фриланса;
-   Создать модули для парсинга работных сайтов;
-   Создать кабинет пользователя для сохранения вакансий/заказов и манипулирования с ними;

## Основные пакеты и версии

| Client Technology | Version | Server Technology | Version | OS             |
| ----------------- | ------- | ----------------- | ------- | -------------- |
| Node.js           | 13.5.0  | Python            | 3.6.9   | Ubuntu 18.04.4 |
| npm               | 6.13.4  | Flask             | 1.1.1   |                |
| Vue.js            | 2.6.11  | Flask-RESTful     | 0.3.8   |                |
| Buefy             | 0.8.12  | ORM Peewee        | 3.13.3  |                |

## Работа с клиентской частью

1. Для начала необходимо с корня проекта перейти в папку с клиентской частью, выполнив команду

```
cd Client
```

2. Выполнить установку зависимотей для проекта (если они еще не установлены)

```
npm install
```

3. Запустить сервер для разработки (hot-reloads)

```
npm run serve
```

После чего в браузере по [адресу http://localhost:8080](http://localhost:8080) должно быть запущено клиентское SPA приложение.

4. Для сборки проекта на продакшен выполнить команду

```
npm run build
```

5. Для линтинга выполнить команду

```
npm run lint
```

## Работа с серверной частью

Обязательным условием запуска всего проекта являеться включение в серверное приложение токенa,  
по которому осуществляеться доступ к [Freelancehunt API 2.0](https://apidocs.freelancehunt.com/?version=latest).  
Чтобы получить токен, зарегистрируйтесь на бирже и перейдите по [ссылке для получения персонального токена](https://freelancehunt.com/my/api).

А дальше нужно создать в корне проекта `Server` файл `.env` (показано на картинке) и поместить туда сгенерированный биржей токен, а также секретный ключ (это строка) для работы Flask-JWT-Extended.

```
#.env
FREELANCEHUNT_API_KEY=ваш токен
JWT_SECRET_KEY = 'ваш_секретеый_ключ'
```

![](https://github.com/VladKurluk/FreelancehuntAPI/blob/master/token.png)

1. Для запуска приложения необходимо с корня проекта перейти в папку с серверной частью, выполнив команду

```
cd Server
```

2. Затем необходимо выполнить активацию виртуального окружения

```
source venv/bin/activate
```

3. После чего нужно установить все зависимости (если они еще не установлены), которые находяться в ф-ле requierments.txt  
   При установке зависимостей может возникнуть ошибка. Тогда в ф-ле `requierments.txt` нужно удалить строку `pkg-resources==0.0.0`

```
pip install -r requierments.txt
```

4. И запустить приложение командой

```
python run.py
```

После чего в браузере по [адресу http://127.0.0.1:5000/api/v1/curent_profile](http://127.0.0.1:5000/api/v1/curent_profile) можно увидеть ответ сервера с полученными данными от биржи freelancehunt.com в JSON формате.
