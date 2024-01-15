#!/usr/bin/env python3
import MySQLdb
import sys


args = sys.argv
kwarg = {
        "host": "localhost",
        "port": 3306,
        "user": args[1],
        "password": args[2],
        "database": args[3]
        }
if __name__ == "__main__":
    db = MySQLdb.connect(**kwarg)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
