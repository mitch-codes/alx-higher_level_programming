#!/usr/bin/python3
"""get info from mysql database but avoid sql injection"""
import sys
import 	MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states")
    results = cur.fetchall()
    for row in results:
        if row[1] == sys.argv[4]:
            print(row)
