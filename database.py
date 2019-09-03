import sqlite3
from random import choice
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)

    return None


def select_random_handset():
    database = "./db/phones.sqlite3"
    # create a database connection

    conn = create_connection(database)
    with conn:
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")

        brand = choice(cur.fetchall())
        cur.execute("SELECT * FROM %s \nORDER BY RANDOM() \n LIMIT 1" % brand[0])
        return cur.fetchone()