#!/usr/bin/python3
"""connect to mysql db"""
import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id")
result = cur.fetchall()

for row in result:
    print(row)

if __name__ == "__main__":
    main()
