#!/usr/bin/python3
"""Module that filters states safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    kwarg = {
            "host": "localhost",
            "port": 3306,
            "user": args[1],
            "password": args[2],
            "database": args[3]
            }
    db = MySQLdb.connect(**kwarg)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s ORDER BY id ASC """,
                (args[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
