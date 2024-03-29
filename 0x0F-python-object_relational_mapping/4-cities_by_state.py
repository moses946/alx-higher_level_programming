#!/usr/bin/python3
"""Module that filters cities by states.
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
    cur.execute(""" SELECT c.id, c.name, s.name
                FROM cities c
                JOIN states s
                ON c.state_id = s.id
                ORDER BY c.id ASC """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
