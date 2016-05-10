import MySQLdb
import time

start = time.time()

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'

db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD)
cur = db.cursor()
db.select_db('taxi')

sql_select = '''select lon,lat from taxi0401 WHERE time_h = 20 and time_m = 37 and time_s = 32 and taxi_id = 203731'''

try:
   # execute sql syntax
   cur.execute(sql_select)
   # fetch all the results
   results = cur.fetchall()
   # sum up column in list
   sum_r = map(sum, zip(*results))
   # length of results
   len_r = len(results)
   # define average function
   def ave(x): return x/len_r
   # compute average
   ave_p = map(ave, sum_r)
   print ave_p

except:
   print "Error: unable to fecth data"

end = time.time()
duration = end - start
print "time duration is: {0}s".format(duration)