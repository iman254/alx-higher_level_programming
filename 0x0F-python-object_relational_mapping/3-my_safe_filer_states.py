#!/usr/bin/python3
"""script that takes in an argument and returns a list of all states wiwith protection from sql injections

if __name __ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], host='localhost', db=sys.argv[3], port=3306)
    cursor = db.cursor()

    query = """ SELECT * FROM states
          WHERE name = %s 
          ORDER BY id ASC"""
    cursor.execute(query, (sys.argv[4]))

    data = cursor.fetchall()
    for row in data: 
        print(row)

    cursor.close()
    db.close()
