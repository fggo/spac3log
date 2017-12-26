# spac3log
text based log app

# Development environment setup

## Use pipenv
use pipenv for virtual environment and package management
```commandline
pipenv install
    # Installing dependencies in
    # ~/.local/share/virtualenvs/project_name-hash/bin/
    
pipenv install django
pipenv install django-bootstrap3
pipenv install dj-database-url
pipenv install whitenoise
pipenv install gunicorn
pipenv install psycopg2

pipenv shell
    # activate this project's virtualenv
```

## Specify python version in Pipfile
```
# -- snip --
[requires]
python_version = "3.6"
```

## Setup PostgreSQL in local
```commandline
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
psql

user=# CREATE USER myprojectuser WITH PASSWORD 'password';

user=# ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
user=# ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
user=# ALTER ROLE myprojectuser SET timezone TO 'UTC';

user=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
user=# \q
```

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

## secret key
on local
```python
# settings.py
SECRET_KEY = os.getenv('SECRET_KEY', default=None)
```

```
# $VIRTUAL_ENV/bin/activate
# -- snip --
SECRET_KEY='YOUR_SECRET_KEY_VALUE'
export SECRET_KEY
```

on heroku
```commandline
heroku config:set SECRET_KEY='YOUR_SECRET_KEY_VALUE'
```

