import MySQLdb
import time

start = time.time()

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'

db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD)
cur = db.cursor()
db.select_db('taxi')

path_0401_ave = 'E:/Slides/LBS/TaxiData/20100401_ave.txt'

# sql_select = '''select lon,lat from taxi0401 WHERE time_h = 20 and time_m = 37 and time_s = 35 and taxi_id = 203714'''
sql_select = '''select * from taxi0401_ave limit 10'''

f = open(path_0401_ave, "w")

try:
   # execute sql syntax
   cur.execute(sql_select)
   end1 = time.time()
   print "select done, time duration {0}".format(end1 - start)
   # fetch all the results
   results = cur.fetchall()
   # print results
   for row in results:
      print row
      str = row
      f.write('%s\n' % str)
      # f.write('%s\n' % row)
      # f.write("\n")
   '''# sum up column in list
   sum_r = map(sum, zip(*results))
   # length of results
   len_r = len(results)
   # define average function
   def ave(x): return x/len_r
   # compute average
   ave_p = map(ave, sum_r)
   print ave_p'''

except:
   print "Error: unable to fecth data"

cur.close()
db.close()
f.close()
end = time.time()
duration = end - start
print "time duration is: {0}s".format(duration)