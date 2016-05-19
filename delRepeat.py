#coding:utf-8
path_0401_HT = 'E:/Slides/LBS/TaxiData/201004010_HT.txt'
# path_0401_HT = 'E:/Slides/LBS/TaxiData/201004010_ave_order_test.txt'
path_0401_HT_uni = 'E:/Slides/LBS/TaxiData/201004010_HT_test.txt'

ciku=open(path_0401_HT,'r')   #打开需要去重文件
xieci=open(path_0401_HT_uni,'w')   #打开处理后存放的文件
cikus=ciku.readlines()
list2 = {}.fromkeys(cikus).keys()     #列表去重方法，将列表数据当作字典的键写入字典，依据字典键不可重复的特性去重
i=1
for line in list2:
	if line[0]!=',':
		# print line[0:-1].decode('utf-8').encode('gbk')   #数据量太多，会出现编码报错。蛋疼
		print  u"写入第："+`i`+u" 个"
		i+=1
		xieci.writelines(line)
xieci.close()
