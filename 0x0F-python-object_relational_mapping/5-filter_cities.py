#!/usr/bin/python3
"""connect to database python"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    result = ""

    cur.execute("SELECT states.id, cities.name, states.name FROM states INNER JOIN cities WHERE states.id=cities.state_id ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        if row[2] == sys.argv[4]:
            result = result + row[1] + ", "
    print(result[0:-2])
