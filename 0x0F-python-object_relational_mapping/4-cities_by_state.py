#!/usr/bin/python3
"""script that lists all the cities in database hbtn_0e_4_usa"""

if __name__ = "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host='localhost', port=3306)
   
    cursor = db.cursor()
    
    query = """SELECT c.id c.name s.name FROM states s, cities c WHERE c.state_id = s.id ORDER BY c.id ASC"""

    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        prnt(row)
    cursor.close()
    db.close()       
