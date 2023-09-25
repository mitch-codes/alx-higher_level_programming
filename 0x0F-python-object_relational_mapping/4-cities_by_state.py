#!/usr/bin/python3
"""use inner join with mysqldb"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT states.id, cities.name, states.name FROM states INNER JOIN cities WHERE states.id = cities.state_id ORDER BY states.id")
    results = cur.fetchall()
    for row in results:
        print(row)
