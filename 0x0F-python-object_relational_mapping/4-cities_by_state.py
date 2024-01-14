#!/usr/bin/python3
"""importing all the necessary modules"""

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
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON states.id = cities.state_id \
            ORDER BY cities.id ASC"
    cur.execute(query)
    allcities = cur.fetchall()
    for city in allcities:
        print(city)
    cur.close()
    conn.close()
