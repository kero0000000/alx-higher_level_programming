#!/usr/bin/python3
"""This project explains linking Python to Database"""
import MYSQLbd
import sys
if __name__=="__main__":
    db=MYSQLdb.connect(host="localhost",user=sys.argv[1],
            passwd=sys.argv[2],db=sys.argv[3],port=3306)
    c = db_cursor()
    c.execute("select * from states")
    rows=c.fetcell()
    for row in rows:
        print(row)
        c.close()
        db.close()
~
