import sys
from dataclasses import dataclass
from mysql.connector import connect, Error
import os
import datetime


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
    'mysql': DB(name='wagtail', user='root', engine='django.db.backends.mysql'),
    'postgres': DB(name='', user='', engine='django.db.backends.postgresql'),
    'sqlite3': DB(name='', user='', engine='django.db.backends.sqlite3'),
    'oracle': DB(name='', user='', engine='django.db.backends.oracle'),
      }

mysql, postgres, sqlite3, oracle = [i for i in db.values()]

# choose engine (mysql, postgres, sqlite3, oracle)
go = mysql    # <-- imported in 'DATABASES' 'dev.py'


def mysql_server_create_db():
    """
    Create MySQL database and .env file with password
    :return: None
    """
    try:
        if (mysql.name and mysql.user) != '':
            try:
                password = input('password: ')
                with connect(
                        host="localhost",
                        user=mysql.user,
                        password=password,
                ) as connection:
                    print(f'--> MySQL server: {connection.get_server_info()}')
                    db_name = mysql.name
                    with connection.cursor() as cursor:
                        cursor.execute(f"""CREATE DATABASE IF NOT EXISTS {db_name} ;""")
                        print(f'--> {db_name} is created')
                    with open("env.txt", "w+") as my_file:
                        my_file.write(f'db_password = {password}')
                    if os.path.exists('.env'):
                        time_stump = datetime.datetime.today().strftime("%d_%m_%Y_%H_%M_%S")
                        os.rename('.env', f'{time_stump}.env')
                        print(f'--> old .env file is renamed {time_stump}.env')
                    os.rename('env.txt', '.env')
                    print('--> .env file is created')
            except Error as e:
                print(f'--> connection aborted\n{e}')
            finally:
                if os.path.exists('env.txt'):
                    os.remove('env.txt')
        else:
            print('--> enter you params in "db" constants with "name" of database\n'
                  '--> and "user" (Login MySQL server)\n'
                  '--> try again')
            sys.exit()
    except KeyboardInterrupt:
        print('\n--> Script aborted')


if __name__ == '__main__':
    mysql_server_create_db()
