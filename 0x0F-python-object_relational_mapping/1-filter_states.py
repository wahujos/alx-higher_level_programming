#!/usr/bin/python3
"""module importation"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    cur = conn.cursor()
    qry = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(qry)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
