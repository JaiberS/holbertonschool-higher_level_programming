#!/usr/bin/python3
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Write a script that lists all states from the database hbtn_0e_0_usa: """
    db = MySQLdb.connect(passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name = %s ORDER BY id ASC""", (argv[4],))
    items = c.fetchall()
    for i in items:
        print(i)
