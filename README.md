# Проект " Трекер привычек"

Данный проект представляет собой веб-приложение для отслеживания полезных привычек. 

## Технологии

- Python
- Django (Django REST framework, Celery)
- PostgresQL (БД для хранения данных)

## Возможности

- Регистрация и авторизация пользователей
- Создание, просмотр, изменение и удаление привычек
- Просмотр списка привычек с пагинацией (количество привычек на странице - 5 штук)
- Просмотр списка публичных привычек
- Отправка напоминаний о привычке в Telegram

## Запуск проекта на Windows:

1. Склонируйте репозиторий https://github.com/Sergo1613/Course_work_7
2. Создайте виртуальное окружение python3 -m venv venv
3. Активируйте виртуальное окружение venv\Scripts\activate
4. Установите зависимости проекта, указанные в файле requirements.txt:
* pip install -r requirements.txt
5. Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample
6. Установите redis локально себе на компьютер, используйте wsl, терминал Ubuntu:
* sudo apt-get update
* sudo apt-get install redis
7. После установки запустите сервер Redis с помощью:
* sudo service redis-server start
* redis-cli
8. командной строке Windows запускайте сервис:
* python manage.py runserver.
9. Запустите Celery для обработки отложенных задач:
* celery -A config worker --pool=solo -l INFO
* celery -A config beat -l info -S django

## Документация API

Документация API доступна после запуска сервера по адресу: http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/docs/
