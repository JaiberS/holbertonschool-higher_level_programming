#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa: """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(passwd=sys.argv[2], db=argv[3], user=argv[1],
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name
              LIKE BINARY "{}" ORDER BY id ASC
              """.format(sys.argv[4]))
    items = c.fetchall()
    if items:
        for i in items:
            print("{}".format(i))
    c.close()
    db.close()
