#!/usr/bin/python3
"""your coments here"""
import MYSQLdb
import sys
if __name__ == "__main__":
db = MYSQLdb.connect(host = "localhost" , user = sys.argv[1],
                            passwd=sys.argv[2] , db= sys.arvg[3], port=3306)
c =db.cursor[]
match = sys.argv[4]
c.execute("select * from states where name like  %s"(match, ))
rows = c.fetchall()
for row in rows:
print(row)
c.close()
db.close()
