#!/usr/bin/python3
"""module imports"""

import MySQLdb
import sys

if __name__ == "__main__":
    hst = 'localhost'
    usr = sys.argv[1]
    pwd = sys.argv[2]
    dtb = sys.argv[3]
    pt = 3306
    conn = MySQLdb.connect(host=hst, user=usr, passwd=pwd, db=dtb, port=pt)
    cur = conn.cursor()
    sname = sys.argv[4]
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON states.id = cities.state_id \
            WHERE states.name = %s"
    cur.execute(query, (sname,))
    res = cur.fetchall()
    for row in res:
        print(row[0], end=' ')
    print()
    cur.close()
    conn.close()
