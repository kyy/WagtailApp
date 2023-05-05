### INCLUDE:

- django-extensions: <https://pypi.org/project/django-extensions/>
- django-debug-toolbar: <https://pypi.org/project/django-debug-toolbar/>
- django-browser-reload: <https://pypi.org/project/django-browser-reload/>
- whitenoise: <https://pypi.org/project/whitenoise/>
- mysql-connector-python: <https://pypi.org/project/mysql-connector-python/>
- mysqlclient: <https://pypi.org/project/mysqlclient/>
- wagtail-color-panel: <https://pypi.org/project/wagtail-color-panel/>
- wagtailmedia: <https://pypi.org/project/wagtailmedia/>
- wagtail-cache: <https://pypi.org/project/wagtail-cache/>
- django-flags / wagtail-flags: <https://pypi.org/project/wagtail-flags/>
- python-webpack-boilerplate: <https://python-webpack-boilerplate.readthedocs.io/en/latest/setup_with_django/>
### INSTALLING:

1. Create virtual env.

```python 
python -m venv /path/to/new/virtual/environment
```

2. Create Git repo.
3. Install MySQL Server: https://dev.mysql.com/downloads/installer/>
4. RUN in:

--> project folder:
```python 
pip install -r requirements.txt
```
--> frontend folder:
```python 
npm install
```

5. Configure 'db' (name, login) in 'db_start.py' for creating MySQL database and run script.

```python 
python db_start.py    
```

```python 
python manage.py migrate
```

```python 
python manage.py createsuperuser
```

```python 
python manage.py runserver
```