file = 'E:/Slides/LBS/TaxiData/20100621.txt'
f = open(file, 'r')
lines = 0
while 1:
	str = f.read(8*1024*1024)
	if not str:
		break
	lines += str.count('\n')
	print "counting {0}".format(lines)
print "the total lines is {0}".format(lines)
