#!/usr/bin/python3
"""use inner join with mysqldb"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[0], passwd=sys.argv[1], db=sys.argv[2])
    cur = db.cursor()

    cur.execute("SELECT states.id, cites.name, states.name FROM states INNER JOIN cities WHERE states.id = cities.state_id ORDER BY state.id")
    results = cur.fetchall()
    for row in results:
        print(row)
