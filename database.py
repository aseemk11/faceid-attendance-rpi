import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

cwd =os.getcwd()
if __name__ == '__main__':
    create_connection(r"{0}\attendence.db".format(cwd))