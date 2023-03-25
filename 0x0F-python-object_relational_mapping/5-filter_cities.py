#!/usr/bin/python3
"""script that takes an adrguement and lists the information regarding the selected argument"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
    cursor = db.cursor()
    
    query = """ SELECT cities.name FROM states INNER JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC"""

    cursor.execute(query)

    data = cursor.fetchall()

    print(", ".join(city[0] from city in data)
    cursor.close()
    db.close()
