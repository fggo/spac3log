# spac3log
text based log app

# pipenv
for virtual environment and package management
```commandline
ls
    .env    requirements.txt
cat requirements.txt
    dj-database-url==0.4.2
    Django==2.0
    django-bootstrap3==9.1.0
    gunicorn==19.7.1
    psycopg2==2.7.3.2
    python-decouple==3.1
    pytz==2017.3
    whitenoise==3.3.1 
pipenv install -r requirements.txt
    # ~/.local/share/virtualenvs/project_name-hash/bin/
    
# activate this project's virtualenv
pipenv shell
```

# Pipfile
```
# -- snip --
[requires]

python_version = "3.6"
```

# PostgreSQL local setup
```commandline
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
psql

user=# CREATE DATABASE myproject; 

user=# CREATE USER myprojectuser WITH PASSWORD 'password';

user=# ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
user=# ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
user=# ALTER ROLE myprojectuser SET timezone TO 'UTC';

user=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
user=# \q
```

# Start django project
```commandline
django-admin.py startproject project_name .
```

# python-decouple
separate code from settings
```commandline
pipenv install python-decouple
```

```text
# .env
SECRET_KEY='your_secret_key'

DEBUG='boolean_value'

ALLOWED_HOSTS=*

DATABASE_NAME='db_name'
DATABASE_USER='db_user'
DATABASE_PASSWORD='db_password'
```

```python
# settings.py
from decouple import Csv, config

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# --snip--
else:
    # Database
    # https://docs.djangoproject.com/en/2.0/ref/settings/#databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': 'localhost',
            'PORT': '',
        }
    }
```

# alternative to python-decouple
```commandline
gedit $VIRTUAL_ENV/bin/activate

    SECRET_KEY='YOUR_KEY'
    export SECRET_KEY
    
    DATABASE_NAME='YOUR_DATABASE'
    DATABASE_USER='YOUR_USER'
    DATABASE_PASSWORD='YOUR_PASSWORD'
    export DATABASE_NAME
    export DATABASE_USER
    export DATABASE_PASSWORD
```
```python
# settings.py
SECRET_KEY = os.getenv('SECRET_KEY', default=None)
```

## secret key on heroku
```commandline
heroku config:set SECRET_KEY='YOUR_SECRET_KEY_VALUE'
```


# Create the database
```commandline
python manage.py migrate
```

# Trouble shooting in Creating postgresql database
"INDENT AUTHENTIFICATION FAILED" [error](https://superuser.com/questions/179238/postgres-ident-authentication-failed)
```commandline
sudo -u postgres psql

postgres=# show hba_file;
    /path/to/pg_hba.conf
postgres=# \q

sudo vim /path/to/pg_hba.conf
    local   all         all                               trust
    host    all         all         127.0.0.1/32          trust
    host    all         all         ::1/128               trust
    host    all         all         0.0.0.0/0             md5
```


# Viewing the project
```commandline
python manage.py runserver
```

# Starting an App
```commandline
python manage.py startapp user_app
```

# Defining models
```python
# models.py 
from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
```
