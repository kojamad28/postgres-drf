# Postgres DRF

This repository provides a Django REST framework project template connected with PostgreSQL database.


## Usage

Clone this repository and build a docker image.
```bash
docker compose build
```

Then migrate the database.
```bash
docker compose run drf python manage.py makemigrations accounts
docker compose run drf python manage.py migrate accounts
docker compose run drf python manage.py migrate
```

Then create a superuser.
```bash
docker compose run django python manage.py createsuperuser
```


## Note

Add migrations directories for git tracking.
```.gitignore
# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
#*/migrations/*
#!*/migrations/__init__.py
```
