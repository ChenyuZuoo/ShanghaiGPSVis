import MySQLdb
import timeit

start = timeit.timeit()


DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'
DB_PORT = '3306'
file_path = 'E:/Slides/LBS/TaxiData/20100621/20100621.txt'

# datavase linking and table creation
# cur is a handle in database
sql_create_table = """CREATE TABLE GPS 
						(date int, taxi_id text(4), company text(5), orientation int, 
						lon float, lat float, velocity float, alti int, passenger tinyint, 
						validity tinyint, date_a tinyint, date_b tinyint, date_c tinyint, time datetime)"""
sql_insert = """insert into GPS (date, taxi_id, company, orientation, lon, lat, 
								velocity, alti, passenger, validity, date_a, date_b, date_c, time) 
								values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

#create db
try:
	# db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD, port = DB_PORT)
	db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD)
	cur = db.cursor()
	cur.execute('create database if not exists taxi')
	db.select_db('taxi')
	cur.execute(sql_create_table)

except MySQLdb.Error, e:
	print "MySQL batabase create error %d: %s" % (e.args[0], e.args[1])


#read data into db
with open(file_path, 'r') as f:
	for line in f:
		str_ori = line #f.readline()
		str_sp = str_ori.split(',')
		time = str_sp[-1].strip(';\n')
		del str_sp[-1]
		str_sp.append(time)
	
		cur = db.cursor()
				# load2db(str_sp);
		cur.execute(sql_insert, str_sp)
		db.commit()

# cur.close()
db.close()

end  = timeit.timeit()
print end-start



# def load2db():
# 	try:
# 		cur.execute(sql_insert, str_sp)
# 		db.commit()
# 	except:
# 		db.rollback()

# def read_data():
# 	try:
# 		with open(file_path, 'r') as f:
# 			for line in f:
# 				str_ori = f.readline()
# 				str_sp = str_ori.split(',')
# 				time = str_sp[-1].strip(';\n')
# 				del str_sp[-1]
# 				str_sp.append(time)
	
# 				# load2db(str_sp);
# 				cur.execute(sql_insert, str_sp)
# 				db.commit()

# 	except MySQLdb.error, e:
# 		print "MySQL batabase load data error %d: %s" % (e.args[0], e.args[1])