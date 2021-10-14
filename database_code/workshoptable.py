# Coby Zimmerman
# Assignment 9
# 11/18/2020
# Python program that reads data from workshops.csv and puts it into a list of dictionaries, and then a table in the
# conference database.
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
    query = "CREATE TABLE IF NOT EXISTS workshops(" \
            "shop_name TEXT," \
            "time_slot INTEGER," \
            "room_number INTEGER," \
            "start_time TEXT," \
            "end_time TEXT" \
            ");"
    cur.execute(query)

    # workshopDict = {}
    # workshopDict['workshopDict'] = []

    # with open('workshops.csv', 'r') as csv_file:
    # reader = csv.DictReader(csv_file)

    # for row in reader:
    # workshopDict['workshopDict'].append(row)
    # print(workshopDict)

    # for key in workshopDict:
    #    print(key, '->', workshopDict[key])

    csv_file = open('workshops.csv', 'r')

    reader = csv.reader(csv_file)

    workshopDict = {}

    workshopDictList = []

    workshopTuple = []

    for line in reader:
        workshopDict['workshop name'] = line[0]
        workshopDict['session'] = line[1]
        workshopDict['room number'] = line[2]
        workshopDict['start time'] = line[3]
        workshopDict['end time'] = line[4]

        workshopDictList.append(workshopDict)
        print(workshopDictList)

        # for key, value in workshopDict.items():
        #    workshopTuple = [tuple()]
        #    print(workshopTuple)

        # cur.executemany("INSERT INTO workshops ('shop_name', 'time_slot', 'room_number', 'start_time', 'end_time') \
        #             VALUES (?,?,?,?,?)", value)

        # for key in workshopDict:
        # workshopTuple = tuple(workshopDict)
        # print(workshopTuple)
        # print(workshopDict[key])
