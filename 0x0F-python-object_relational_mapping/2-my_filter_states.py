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
    sname = sys.argv[4]
    qr = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC" \
        .format(sname)
    cur.execute(qr)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
