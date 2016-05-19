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
fw.write(str_r)
print str_r

for str_l in fl:
    str_r = fr.readline()
    # print str_r
    sp_l = str_l.split()
    sp_r = str_r.split()
    if (sp_l[0] != sp_r[0]):
        fw.write(str_l)
        fw.write(str_r)
    else:
        time_l = int(sp_l[1].strip(",")) * 3600 + int(sp_l[2].strip(",")) * 60 + int(sp_l[3].strip(","))
        time_r = int(sp_r[1].strip(",")) * 3600 + int(sp_r[2].strip(",")) * 60 + int(sp_r[3].strip(","))
        print "time diff", time_r - time_l
        if ((time_r - time_l) > 60):
            fw.write(str_l)
            fw.write(str_r)
# str_l = f.readline()
#
# sp_l = str_l.split()
# sp_r = str_r.split()
# # print "sp_l original", sp_l
# # sp_l = sp_l.strip(",")
# # print "sp_l[3] strip", int(sp_l[3].strip(","))
#
# # print "time_h",sp_l,sp_l[1], sp_l[2]
# time_l = int(sp_l[1].strip(",")) * 3600 + int(sp_l[2].strip(",")) * 60 + int(sp_l[3].strip(","))
# time_r = int(sp_r[1].strip(",")) * 3600 + int(sp_r[2].strip(",")) * 60 + int(sp_r[3].strip(","))
# # tl_s = sp_l[3]
# # print "int sp time_s", sp_l[3], tl_s
#
# # print type(tl_s)
# # print str_l[1], str_l[2], str_l[3]
# # print str_r[1], str_r[2], str_r[3]
# # print type(int(sp_l[1]))
# print "time diff", time_r-time_l
# if ((time_r-time_l) > 60):
#     fw.write(str_l)
#     fw.write(str_r)
# # fw.write(str_r)

# for str_l in f:
#     time = str_l[1]*3600 + str_l[2]*60 + str_l[3]
#     time_n = str_r[1]*3600 + str_r[2]*60 + str_r[3]
#     if (str_l[1]*3600 + str_l[2]*60 + str_l[3])

fw.close()
fl.close()
fr.close()

end = time.time()
duration = end - start
print "time duration is: {0}min".format(duration/60)