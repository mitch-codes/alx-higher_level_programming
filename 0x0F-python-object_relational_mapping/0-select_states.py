#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
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
