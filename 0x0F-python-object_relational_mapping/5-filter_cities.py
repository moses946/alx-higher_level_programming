#!/usr/bin/python3
"""Module that lists all cities of a state.
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
    cur.execute("""SELECT name
                FROM cities
                WHERE state_id = (
                SELECT id
                FROM states
                WHERE name = %s)""", (args[4],))
    rows = cur.fetchall()
    ans = []
    for row in rows:
        ans.append(row[0])
    print(', '.join(ans))
    cur.close()
    db.close()
