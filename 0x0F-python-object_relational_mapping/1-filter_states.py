#!/usr/bin/python3
"""selct id and name where name follows pattern"""
import 	MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.agrv[2], port=3306, db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT id, name FROM states WHERE name LIKE %s ORDER BY id",("N%"))
rows = cur.fetchall()
for row in rows:
    print(row)

if __name__ == "__main__":
    main()
