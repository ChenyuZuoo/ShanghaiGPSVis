import MySQLdb
import time

start = time.time()

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'
DB_DB = 'taxi'

db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD, db=DB_DB, cursorclass=MySQLdb.cursors.SSCursor)
cur = db.cursor()
db.select_db('taxi')

sql_select = '''select taxi_id,lon,lat from taxi0401'''

try:
   # execute sql syntax
   cur.execute(sql_select)
   # fetch all the results
   results = cur.fetchall()
   # sum up column in list
   '''sum_r = map(sum, zip(*results))
   # length of results
   len_r = len(results)
   # define average function
   def ave(x): return x/len_r
   # compute average
   ave_p = map(ave, sum_r)
   print ave'''
   length = len(results)
   for(i = 0; i < length; i++):
       return

except:
   print "Error: unable to fecth data"

cur.close()
db.close()
f.close()

end = time.time()
duration = end - start
print "time duration is: {0}s".format(duration)