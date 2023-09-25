#!/usr/bin/python3
"""script that uses user input in mysql"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name={}".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
