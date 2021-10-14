# Coby Zimmerman
# Assignment 9
# 11/18/2020
# Python program that reads data from users.csv and adds it to users table in conference database
import sqlite3
import csv


class AccessDatabase:

    def __init__(self):
        self.dbname = 'conference.sqlite'
        return

    def __enter__(self) -> 'cursor':
        self.conn = sqlite3.connect(self.dbname)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_value, ex_trace):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return


# Creates table if it doesn't already exist
with AccessDatabase() as cur:
    query = "CREATE TABLE IF NOT EXISTS users(" \
            "id INTEGER PRIMARY KEY AUTOINCREMENT," \
            "username TEXT," \
            "firstname TEXT," \
            "lastname TEXT," \
            "password TEXT" \
            ");"
    cur.execute(query)

    # reads file, puts data in list of tuples, and then places the data into the users table
    with open('users.csv', 'r') as csv_file:
        usersTuple = [tuple(line) for line in csv.reader(csv_file)]
        # print(nomineeTuple)

        cur.executemany("INSERT INTO users ('username', 'firstname', 'lastname', 'password') \
                         VALUES (?,?,?,?)", usersTuple)
