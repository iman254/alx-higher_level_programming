#!/usr/bin/python3
""" a script that lists all the states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    rows = c.fetchall()
    for rows in rows:
        print(row)
    c.close()
    db.close()