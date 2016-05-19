import time

start = time.time()
path_0401_ave = 'E:/Slides/LBS/TaxiData/201004010_ave_order.txt'
# path_0401_ave = 'E:/Slides/LBS/TaxiData/201004010_ave_order_test.txt'
path_0401_HT = 'E:/Slides/LBS/TaxiData/201004010_HT.txt'
fl = open(path_0401_ave, "r")
fr = open(path_0401_ave, "r")
fw = open(path_0401_HT, "w")

# fr.readline()
str_r = fr.readline()
print str_r

for str_l in fl:
    str_r = fr.readline()
    sp_l = str_l.split()
    sp_r = str_r.split()
    # extract the beginning and ending od a taxi
    if (sp_l[0] != sp_r[0]):
        fw.write(str_l)
        fw.write(str_r)
    else:  #calculate time difference
        time_l = int(sp_l[1].strip(",")) * 3600 + int(sp_l[2].strip(",")) * 60 + int(sp_l[3].strip(","))
        time_r = int(sp_r[1].strip(",")) * 3600 + int(sp_r[2].strip(",")) * 60 + int(sp_r[3].strip(","))
        print "time diff", time_r - time_l
        if ((time_r - time_l) > 60):
            fw.write(str_l)
            fw.write(str_r)

fw.close()
fl.close()
fr.close()

end = time.time()
duration = end - start
print "time duration is: {0}min".format(duration/60)