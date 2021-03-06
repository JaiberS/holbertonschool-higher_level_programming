#!/usr/bin/python3
""" Write a script lists all states from the database hbtn_0e_0_usa: """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Write a script lists all states from the database hbtn_0e_0_usa: """
    db = MySQLdb.connect(passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.name FROM states, cities
    WHERE states.id = cities.state_id and states.name = %s
    ORDER BY cities.id ASC""", (argv[4],))
    items = c.fetchall()
    str0 = ""
    for i in items:
        str0 = str0 + i[0] + ", "
    print(str0[0:-2])
    c.close()
    db.close()
