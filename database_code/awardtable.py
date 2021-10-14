# Coby Zimmerman
# Assignment 9
# 11/18/2020
# Python program that reads data from awards.csv and inserts it into awards table in conference database
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
    query = "CREATE TABLE IF NOT EXISTS nominees(" \
            "id INTEGER PRIMARY KEY AUTOINCREMENT," \
            "nominee_name TEXT," \
            "description TEXT," \
            "image_name TEXT," \
            "curr_votes INTEGER" \
            ");"
    cur.execute(query)

    # Reads data, puts it in a list of tuples, and inserts it into nominees table
    with open('awards.csv', 'r') as csv_file:
        nomineeTuple = [tuple(line) for line in csv.reader(csv_file)]
        # print(nomineeTuple)

        cur.executemany("INSERT INTO nominees ('nominee_name', 'description', 'image_name', 'curr_votes') \
                         VALUES (?,?,?,?)", nomineeTuple)
