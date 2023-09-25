#!/usr/bin/python3
"""selct id and name where name follows pattern"""
import 	MySQLdb
import sys

db = MySQLdb.connect(user=root, passwd=PASS, port=3306, db=hbtn_0e_0_usa)
cur = db.cursor()

cur.execute("SELECT id, name FROM states WHERE name LIKE %s ORDER BY id",("N%"))
rows = cur.fetchall()
for row in rows:
    print(row)

if __name__ == "__main__":
    main()
