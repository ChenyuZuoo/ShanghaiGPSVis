path_0401 = 'E:/Slides/LBS/TaxiData/20100401.txt'
#count total line number of file
f = open(path_0401, 'r')

cline = 0
while 1:
    buffer = f.read(8*1024*1024)
    if not buffer:
        break
    cline += buffer.count("\n")
    print cline

print cline
