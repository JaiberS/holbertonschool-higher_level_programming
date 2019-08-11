#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa: """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    """ Write a script lists all states from the database hbtn_0e_0_usa: """
    db = MySQLdb.connect(passwd=argv[2], db=argv[3], user=argv[1],
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM states, cities
    WHERE states.id = cities.state_id ORDER BY cities.id ASC""")
    items = c.fetchall()
    for i in items:
        print(i)
    c.close()
    db.close()
