import MySQLdb
import time

start = time.time()

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'
DB_DB = 'taxi'

# db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD, db=DB_DB, cursorclass=MySQLdb.cursors.SSCursor)
db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD, db=DB_DB)
cur = db.cursor()
db.select_db('taxi')
'''taxi_id,lon,lat'''
sql_select = '''select * from taxi04010_ave_order'''

# path_0401_ave = 'E:/Slides/LBS/TaxiData/201004010_ave_order.txt'
path_0401_ave = 'E:/Slides/LBS/TaxiData/201004010_ave_order_test.txt'
f = open(path_0401_ave, "w")

try:
   # execute sql syntax
   cur.execute(sql_select)
   # fetch all the results
   results = cur.fetchall()

   for row in results:
      print row
      stri = str(row)
      print type(stri)
      # line = stri.strip("(").strip(")").strip("'")
      line = "{0}, {1}, {2}, {3}, {4}, {5}".format(row[0], row[1], row[2], row[3], row[4], row[5])
      # print "striped %s" % line
      f.write(line + "\n")

except Exception,e:
   print e

cur.close()
db.close()
f.close()

end = time.time()
duration = end - start
print "time duration is: {0}s".format(duration)