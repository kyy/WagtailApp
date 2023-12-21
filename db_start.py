import sys
from dataclasses import dataclass
from mysql.connector import connect, Error
import os
from pathlib import Path
from dotenv import set_key

"""
Autoconfiguration 'DATABASES' for settings 'dev.py and saving secure password in .env'
"""


@dataclass(frozen=True)
class DB:
    """
    name: name of database for creating
    user: username in MySQL server
    """
    name: str
    user: str
    engine: str


# db constants, enter your params
db = {
    'mysql': DB(name='', user='', engine='django.db.backends.mysql'),
    'postgres': DB(name='', user='', engine='django.db.backends.postgresql'),
    'sqlite3': DB(name='', user='', engine='django.db.backends.sqlite3'),
    'oracle': DB(name='', user='', engine='django.db.backends.oracle'),
}

mysql, postgres, sqlite3, oracle = [i for i in db.values()]

# choose engine (mysql, postgres, sqlite3, oracle)
go = mysql  # <-- imported in 'DATABASES' 'dev.py'


def mysql_server_create_db():
    """
    Create MySQL database and .env file with password
    :return: None
    """
    try:
        if (mysql.name and mysql.user) != '':
            password = input('password: ')
            with connect(host="localhost", user=mysql.user, password=password) as connection:
                print(f'--> MySQL server: {connection.get_server_info()}')
                db_name = mysql.name
                with connection.cursor() as cursor:
                    cursor.execute(f"""CREATE DATABASE IF NOT EXISTS {db_name} ;""")
                    print(f'--> {db_name} is created')

                if not os.path.exists('.env'):
                    with open(".env", "w+") as my_file:
                        print('--> .env file is created')

                if os.path.exists('.env'):
                    env_file_path = Path(".env")
                    env_file_path.touch(mode=0o600, exist_ok=True)
                    set_key(dotenv_path=env_file_path, key_to_set="DB_PASSWORD", value_to_set=password)
            sys.exit()
        elif mysql.name == mysql.user == '':
            print('empty name or user!')
    except KeyboardInterrupt:
        print('\n--> Script aborted')


if __name__ == '__main__':
    mysql_server_create_db()
