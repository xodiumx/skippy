# Skippy

![FastAPI](https://img.shields.io/badge/FastAPI-44944A?style=for-the-badge&logo=fastapi&logoColor=white)

## Description

**Skippy** - платформа для записи просмотренных фильмов и сериалов, с возможностью получения уведомлений о выходе новых серий и новых фильмов, а также удобным сохранением закладок для будущего просмотра =)

### Available features:

- Регистрация пользователя
- Аутентификация пользователя через `JWT`

### TODO List
- Доп. возможности в приложении users (обновление пароля и др.)
- Создание моделей фильмов и сериалов
- Создание endpoint-ов для записи просмотренного контента
- Настроить админку
- Endpoint избранного
- Выгрузка контента через csv или другим способом
- Настройка уведомлений на почту и в телеграм
- Настройка удобного запуска через docker
- Front часть
- и др.

## Download and start app

1. Необходимо склонировать репозиторий
```
git clone git@github.com:xodiumx/skippy.git
```
2. Cоздать и активировать виртуальное окружение:
```
py -3.10 -m venv venv
```
```
python -m pip install --upgrade pip
source venv/Scripts/activate или source env/bin/activate
```
3. Установить зависимости из файла `requirements.txt`
```
python -m pip install --upgrade pip \
&& pip install -r requirements.txt
```
4. Создать файл `.env` пример:
```
SECRET_KEY=KDOuifes@@ruy432iiupupifesUIPDASBDKGA3dko5OwCXyli1Il8M
USER_SECRET_KEY=KDOuifehtryuoigreuo@4327TG!!*&g8cbSAidsamopi~!^

SERVER_HOST=127.0.0.1
SERVER_PORT=8000

DB_HOST=localhost
DB_PORT=5432
DB_NAME=skippy
DB_USER=postgres
DB_PASS=admin

JWT_SECRET=KDO8l12ZMhw9MHv1PzPRhyVKGA3dko5OwCXyli1Il8M
JWT_ALGORITHM=HS256
JWT_EXPIRATION=3600

ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin
```
5. запустить файл `__main__.py`
