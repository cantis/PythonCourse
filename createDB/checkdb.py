''' Code Challenge, print out all the records and explain why they are not as expected. '''
import sqlite3

DB = sqlite3.connect("createDB/contacts.sqlite")

NAMETOGET = input("Name To Retrieve: ")

for rows in DB.execute("select * from contacts where name = ?", (NAMETOGET,)):
    print(rows)

DB.close()
