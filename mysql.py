#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="10.49.130.37",
                     user="cedittec",
                      passwd="server",
                      db="biogasViejo")


cur = db.cursor() 
cur.execute("SELECT * FROM biofiltro")

for row in cur.fetchall() :
    print row