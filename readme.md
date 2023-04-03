
### INCLUDE:
  - django-extensions 3.2.1: <https://pypi.org/project/django-extensions/>
  - django-debug-toolbar 3.8.1: <https://pypi.org/project/django-debug-toolbar/>
  - django-browser-reload 1.7.0: <https://pypi.org/project/django-browser-reload/>
  - whitenoise 6.4.0: <https://pypi.org/project/whitenoise/>
  - fontawesome-free 5.15.4: <https://pypi.org/project/fontawesome-free/>
  - mysql-connector-python 8.0.32: <https://pypi.org/project/mysql-connector-python/> 
  - mysqlclient 2.1.1: <https://pypi.org/project/mysqlclient/> 

### INSTALLING:
1. Create virtual env. 
```python 
python -m venv /path/to/new/virtual/environment
```
2. Create Git repo.
3. Install MySQL Server: https://dev.mysql.com/downloads/installer/>
4. Configure 'db' (name, login) in 'db_start.py' for creating MySQL database and run script.
```python 
python db_start.py    
```
5. RUN in project folder:
```python 
python pip install -r requirements.txt
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