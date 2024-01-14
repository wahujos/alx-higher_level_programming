#!/usr/bin/python3
"""Important module importations"""

import MySQLdb
import sys

if __name__ == "__main__":
    hst = 'localhost'
    usr = sys.argv[1]
    pd = sys.argv[2]
    dtb = sys.argv[3]
    pt = 3306
    sname = sys.argv[4]
    conn = MySQLdb.connect(host=hst, user=usr, passwd=pd, db=dtb, port=pt)
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id"
    cur.execute(query, (sname,))
    allstates = cur.fetchall()
    for state in allstates:
        print(state)
    cur.close()
    conn.close()
