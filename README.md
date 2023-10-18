## Django-приложение “Образовательные модули”

Этот проект представляет собой простое Django приложение, разработанное с использованием Django и Django REST Framework.
Он предоставляет API для управления образовательными модулями.

### Технологии

- Django
- Django REST Framework
- Python
- Docker
- Postgres

### Доступные эндпоинты API

* `GET /api/educational_modules/`: получение всех модулей
* `GET /api/educational_modules/<int:pk>/`: Получение одного модуля
* `POST /api/educational_modules/`: Создание модуля
* `PUT /api/educational_modules/<int:pk>/`: Обновление модуля
* `DELETE /api/educational_modules/<int:pk>/`: Удаление модуля

### Инструкция по запуску приложения:
_Для запуска проекта необходимо клонировать репозиторий, создать и активировать виртуальное окружение:_
```
python3 -m venv venv

venv/Scripts/activate - активация на Windows
source venv/bin/activate - активация на Mac и Linux
```
_Установить зависимости:_
```
pip install -r requirements.txt
```
_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample:_
```
SECRET_KEY=

# настройка базы данных
POSTGRES_ENGINE=
POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
_Выполнить миграции:_
```
python3 manage.py migrate
```
_Для создания суперпользователя запустить команду:_
```
python3 manage.py csu
```
_Для запуска приложения:_
```
python3 manage.py runserver
```
_Для тестирования проекта запустить команду:_
```
python3 manage.py test
```
_Для создания образа из Dockerfile и запуска контейнера запустить команду:_
```
docker-compose up --build
```
_или_
```
docker-compose up -d --build
```
### API-документация проекта: http://127.0.0.1:8000/swagger/

### Аутентификация

API эндпоинты защищены аутентификацией. Вы можете использовать токены аутентификации для доступа к защищенным
эндпоинтам. Чтобы получить токен, выполните POST-запрос на /api/token/ с параметрами email и password. Полученный
токен должен быть передан в заголовке Authorization для доступа к защищенным ресурсам.

### Автор

* **Исхаков Денис** - [Iskhakov Denis](https://github.com/denimani)
