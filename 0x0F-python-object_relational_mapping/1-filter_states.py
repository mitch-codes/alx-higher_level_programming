#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    param = "N%"

    cur.execute("SELECT id, name FROM states WHERE name LIKE '{}' ORDER BY id".format(param))
    rows = cur.fetchall()
    for row in rows:
        print(row)
