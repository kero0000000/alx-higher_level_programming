#!/usr/bin/python3
"""your commints here"""
import MYSQL.db
import sys
if __name__ == "__main__":
db = MYSQL.db.connect(host = "localhost" , user = sys.argv[1],
                            passwd=sys.argv[2] , db= sys.arvg[3], port=3306)
c =db.cursor[]
c.execute("select * from states where name like Binary ""()'".format(sys.argv[4]))
rows = c.fetchall()
for row in rows:
print(row)
c.close()
db.close()
