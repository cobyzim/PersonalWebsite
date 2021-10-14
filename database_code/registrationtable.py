# Coby Zimmerman
# Assignment 9
# 11/18/2020
# Python program that reads data from registrant_data.csv and places it into registrants table in the conference
# database using a class called Registrant and objects from this class.
import sqlite3
import csv


def db_connect():
    db_name = 'conference.sqlite'
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


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


# Creates a table if it doesn't already exist
with AccessDatabase() as cur:
    query = "CREATE TABLE IF NOT EXISTS registrants(" \
            "registration_date TEXT," \
            "title TEXT," \
            "firstname TEXT," \
            "lastname TEXT," \
            "address TEXT," \
            "city TEXT," \
            "state TEXT," \
            "zip INTEGER," \
            "telnum TEXT," \
            "email TEXT," \
            "companysite TEXT," \
            "companypos TEXT," \
            "companyname TEXT," \
            "meal TEXT," \
            "cardfname TEXT," \
            "cardlname TEXT," \
            "cardtype TEXT," \
            "cardnum INTEGER," \
            "cvv INTEGER," \
            "expyear INTEGER," \
            "expmonth INTEGER," \
            "workshopone TEXT," \
            "workshoptwo TEXT," \
            "workshopthree TEXT" \
            ");"

    cur.execute(query)


# Registrant class with __init__ constructor
class Registrant:
    def __init__(self, registration_date, title, fname, lname, address, city, state, zip, telnum, email, companysite,
                 companypos, companyname, meal, cardfname, cardlname, cardtype, cardnum, cvv, expdate, expmonth,
                 workshopone, workshoptwo, workshopthree):
        self.registration_date = registration_date
        self.title = title
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.telnum = telnum
        self.email = email
        self.companysite = companysite
        self.companypos = companypos
        self.companyname = companyname
        self.meal = meal
        self.cardfname = cardfname
        self.cardlname = cardlname
        self.cardtype = cardtype
        self.cardnum = cardnum
        self.cvv = cvv
        self.expdate = expdate
        self.expmonth = expmonth
        self.workshopone = workshopone
        self.workshoptwo = workshoptwo
        self.workshopthree = workshopthree

    # def registrant_data(self, whatevs):
    #    print(whatevs)


# reads data from file into fields of the class
with open('registrant_data.csv') as csv_file:
    for line in csv_file.readlines():
        newline = line.rstrip("\n")
        regFields = newline.split(',')
        registrationDate = regFields[0]
        title = regFields[1]
        fname = regFields[2]
        lname = regFields[3]
        address = regFields[4] + ' ' + regFields[5]
        city = regFields[6]
        state = regFields[7]
        zip = regFields[8]
        telnum = regFields[9]
        email = regFields[10]
        companysite = regFields[11]
        companypos = regFields[12]
        companyname = regFields[13]
        meal = regFields[14]
        cardfname = regFields[15]
        cardlname = regFields[16]
        cardtype = regFields[17]
        cardnum = regFields[18]
        cvv = regFields[19]
        expdate = regFields[20]
        expmonth = regFields[21]
        workshopone = regFields[22]
        workshoptwo = regFields[23]
        workshopthree = regFields[24]

        # makes list of Registrant objects
        regList = []
        regList.append(
            Registrant(registrationDate, title, fname, lname, address, city, state, zip, telnum, email, companysite,
                       companypos, companyname, meal, cardfname, cardlname, cardtype, cardnum, cvv, expdate, expmonth,
                       workshopone, workshoptwo, workshopthree))

        dataList = []

        # puts fields of registrant class into list of tuples to then be inserted into the table
        for obj in regList:
            dataList.append(
                tuple((obj.registration_date, obj.title, obj.fname, obj.lname, obj.address, obj.city, obj.state,
                       obj.zip, obj.telnum, obj.email, obj.companysite, obj.companypos, obj.companyname,
                       obj.meal, obj.cardfname, obj.cardlname, obj.cardtype, obj.cardnum, obj.cvv, obj.expdate,
                       obj.expmonth, obj.workshopone, obj.workshoptwo, obj.workshopthree)))

        conn = db_connect()
        cur = conn.cursor()
        cur.executemany("INSERT INTO registrants ('registration_date', 'title', 'firstname', 'lastname', \
                         'address','city', 'state', 'zip', 'telnum', 'email', 'companysite', 'companypos', \
                         'companyname', 'meal', 'cardfname', 'cardlname', 'cardtype', 'cardnum', 'cvv', \
                         'expyear', 'expmonth', 'workshopone', 'workshoptwo', 'workshopthree') \
                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", dataList)
        conn.commit()
        conn.close()
