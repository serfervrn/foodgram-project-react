# Дипломная работа Foodgram
![Yamdb_workflow](https://github.com/serfervrn/foodgram-project-react/workflows/for_main_branch_workflow.yml/badge.svg)

## Описание

Проект Foodgram - сервис для публикации кулинарных рецептов. 

Демоверсия сайта: http://158.160.6.30/

Документация API: http://158.160.6.30/api/docs/

Админка: 
- login: admin@admin.com
- password: admin

Возможности сервиса:

- Регистрация пользователей.
- Создание, Изменение, Удаление рецептов.
- Добавление рецептов в избранное и простмотр всех избранных рецептов.
- Фильтрация рецептов по тегам.
- Подписка на авторов и просмотр рецептов определенного автора.
- Добавление рецептов и формирование списка покупок для их приготовления.

### Шаблон наполнения env-файла
```
DB_NAME='postgres' # имя базы данных
POSTGRES_USER='postgres' # логин для подключения к базе данных
POSTGRES_PASSWORD='postgres' # пароль для подключения к БД
DB_HOST='db' # название сервиса (контейнера)
DB_PORT='5432' # порт для подключения к БД
SECRET_KEY='...' # секретный ключ Django-проекта
```

### Запуск проекта
 - Запустите доккер:
   ```
   sudo docker-compose up
   ```
- Соберите статические файлы:
   ```
  sudo docker-compose exec backend python manage.py collectstatic --noinput
   ```
- Примените миграции:
  ```
  sudo docker-compose exec backend python manage.py migrate --noinput
  ```
- Создать суперпользователя Django:
  ```
  sudo docker-compose exec backend python manage.py createsuperuser
  ```


### Используемые технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

[//]: # ([![GitHub%20Actions]&#40;https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions&#41;]&#40;https://github.com/features/actions&#41;)

[//]: # ([![Yandex.Cloud]&#40;https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud&#41;]&#40;https://cloud.yandex.ru/&#41;)

### Автор проекта:
Осенев Сергей