import MySQLdb
import time

start = time.time()

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWD = 'zuochenYU!@'

count = 1
countLine = 0

#file path
path_0621 = 'E:/Slides/LBS/TaxiData/20100621.txt'
path_0401 = 'E:/Slides/LBS/TaxiData/20100401.txt'
path_0401_ave = 'E:/Slides/LBS/TaxiData/20100401.txt'
path_e = 'E:/Slides/LBS/TaxiData/exprdata.txt'

#sql create table syntax
# sql_create_table = """CREATE TABLE taxi21_1
# 						(id MEDIUMINT NOT NULL AUTO_INCREMENT, date VARCHAR(16), taxi_id VARCHAR(16), company VARCHAR(2), orientation int,
# 						lon float, lat float, velocity float, alti int, passenger tinyint,
# 						validity tinyint, time_h tinyint, time_m tinyint, time_s tinyint, PRIMARY KEY (id))"""
sql_create_table = """CREATE TABLE taxi0401
						(taxi_id VARCHAR(16), lon float, lat float, passenger tinyint, time_h tinyint, time_m tinyint, time_s tinyint)"""
# connect to MySQL
db = MySQLdb.connect(host = DB_HOST, user = DB_USER, passwd = DB_PASSWD)
cur = db.cursor()
# cur.execute('create database if not exists taxi')
db.select_db('taxi')
cur.execute("drop table taxi0401")
cur.execute(sql_create_table)

#count total line number of file
f = open(path_0401, 'r')
def Lines():
	#ff = open(path_e, 'r')
	cline = 0
	while 1:
		buffer = f.read(8*1024*1024)
		if not buffer:
			break
		cline += buffer.count("\n")
		print cline

	f.seek(0)
	return cline

#read one line and complete insert sentence
def commit2db(f, sql_insert):
	#insert last row, sql append without ","
	str_ori = f.readline()
	str_sp = str_ori.split(',')
	# if (str_sp[9] == "0"):
	# 	sql_insert = sql_insert[:-1]
	# 	print "committed to db"
	# 	cur.execute(sql_insert)
	# 	db.commit()
	# 	return
	time_h = str_sp[-1][-10:-8]  # formate 'datetime' into 'time'
	time_m = str_sp[-1][-7:-5]
	time_s = str_sp[-1][-4:-2]
	sql_insert += " ('{0}',{1},{2},{3},{4},{5},{6})".format(str_sp[1],str_sp[4],str_sp[5],str_sp[8],time_h,time_m, time_s)

	print "committed to db"
	cur.execute(sql_insert)
	db.commit()

file_line = Lines()

def jump2line(line):
	lineC = 0
	while ( lineC < line):
		# load lines from a specific line, using when database over loaded for one time
		f.readline()
		lineC += 1
	return f

#read lines in file and write insert statements
#insert several lines at one time
class FoundException(Exception): pass

try:
	#if read to the penultimate line line, then go to jump2line function and jump out of loop
	#f = jump2line(105)
	while(1):
		sql_insert = """insert into taxi0401 (taxi_id, lon, lat, passenger, time_h, time_m, time_s)
											values """
		while(count < 200):
			str_ori = f.readline()
			print str_ori
			#if read to the penultimate line line, change the stop control,
			if (countLine * 200 + count) == (file_line - 1):
				str_sp = str_ori.split(',')
				# if (str_sp[8] == "0"):
				# 	sql_insert = sql_insert[:-1]
				# 	commit2db(f, sql_insert)
				# 	raise FoundException
				time_h = str_sp[-1][-10:-8]  # format 'datetime' into 'time'
				time_m = str_sp[-1][-7:-5]
				time_s = str_sp[-1][-4:-2]
				sql_insert += " ('{0}',{1},{2},{3},{4},{5},{6}),".format(str_sp[1],str_sp[4],str_sp[5],str_sp[8],time_h,time_m, time_s)
				commit2db(f, sql_insert)
				raise FoundException
			str_sp = str_ori.split(',')
			print str_sp[8]
			if(str_sp[8] == "0"):
				continue
			time_h = str_sp[-1][-10:-8]  #formate 'datetime' into 'time'
			time_m = str_sp[-1][-7:-5]
			time_s = str_sp[-1][-4:-2]
			sql_insert +=" ('{0}',{1},{2},{3},{4},{5},{6}),".format(str_sp[1],str_sp[4],str_sp[5],str_sp[8],time_h,time_m, time_s)
			count = count +1
		commit2db(f, sql_insert)

		countLine += 1
		print "load {0} lines".format(countLine * 200)
		count = 1
except FoundException:
	print "the end of file"
	
cur.close()
db.close()
f.close()

end = time.time()
print "total duration: {0} seconds".format(end - start)