#!/usr/bin/python3
""" a script that lists all the states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host= 'localhost', port = 3306)
        except MySQLdb.Error:
            print("connection error")

        c = db.cursor()
        try:

            c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
            rows = c.fetchall()
            for row in rows:
                print(row)
        except MySQLdb.Error:
            print("execution Error)
        c.close()
        db.close()
