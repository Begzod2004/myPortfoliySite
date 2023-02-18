### Creator [Begzod2004](httos://github.com/Begzod2004)
<hr>
<br>
<br>

# Features

-  Django 3.2+
-  Django REST framework 3.10+
-  Environment variables loading with [django-dotenv](https://github.com/jpadilla/django-dotenv)
-  Generating documentation from OpenAPI schemas with [drf-yasg](https://github.com/axnsan12/drf-yasg/)
-  CORS support with [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
-  Exposing application information over [Browseable API](https://www.django-rest-framework.org/topics/browsable-api/)

# Installation

```bash
$ git clone https://github.com/Begzod2004/myPortfoliySite.git
$ pip install -r requirements.txt
$ python manage.py make migrations
$ python manage.py migrate
$ python manage.py runserver
```

# Configuring applications

Django apps to be placed inside `apps/` directory. To work with this configuration you need first to run the `startapp`command inside this directory:


## Core settings

| Variable        | Description                                                                          | Default   |
| --------------- | ------------------------------------------------------------------------------------ | :-------: |
| `DEBUG`         | Turns on/off debug mode. Never deploy a site into production with `DEBUG` turned on  | `true`    |
| `ALLOWED_HOSTS` | List, splitted by comma, of host/domain that your application can serve               | `*`       |


#### Example
```
DEBUG=True
ALLOWED_HOSTS=www.example.com,.subdomain.com
```

## Database settings
To know how configure databases in a Django application, see the [documentation](https://docs.djangoproject.com/en/3.2/ref/databases/)


| Variable         | Description                                                                          | Default     |
| ---------------  | ------------------------------------------------------------------------------------ | :---------: |
| `DB_ENGINE`      | Database backend to use. Options are: `mysql`, `oracle`, `postgresql`, `postgresql_psycopg2`,  `sqlite3`         | `sqlite3`    |
| `DB_NAME`        | The name of database to use                                                          | `db.sqlite3`|
| `DB_HOST`        | Which host to use when connecting to the database                                    | -           |
| `DB_PORT`        | The port to use when connecting to the database                                      | -           |
| `DB_USER`        | The username to use when connecting to the database                                  | -           |
| `DB_PASSWORD`    | The password to use when connecting to the database                                  | -           |
| `DB_CONN_MAX_AGE`| The lifetime of a database connection, in seconds                                    | `0`         |

Depending on your `DB_ENGINE` variable you should install another package like `psycopg2` or `cx_Oracle` for PostgreSQL and Oracle databases, respectively.

# Project structure                                                     

```
[MYPORTFOLIYSITE]  
│ 
|── config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
|   
│    
│── mysite
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   |── models.py
|   |── serializer.py
|   |── tests.py
|   |── urls.py
│   └── viows.py
|   
├── .gitignore
├── manage.py
├── README.md
|── requirements.txt
└── static
```
