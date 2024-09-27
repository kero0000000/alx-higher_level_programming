#!/usr/bin/python3
"""your coment here"""
import MYSQLdb
import sys
if __name__ == "__main__":
db = MYSQLdb.connect(host="localhost", user= sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], port=3306)
c = db.cursor()
c.execute("""select cities.id, cities.name, states.name from
                              cities inner join states on states.id=cities.state_id""")
rows = c.fetchall()
for row in rows:
print(row)
c.close()
db.close()
