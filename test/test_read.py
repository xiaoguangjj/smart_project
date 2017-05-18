#encoding:utf-8

import sys
sys.path.append('/home/pi/project_rfid/smart_project/smart_project/site')

import read
import read_two

#注意s50卡数据块读时需要从后往前读

data = []
result = read_two.read_second_block(True)
result_two = result
result = read.read_first_block(True)
com_data = result+result_two
print 'result:',result
le = result.index(58)
for i in range(len(com_data)):
    if i < le:
        data.append(com_data[i])
    else:
        if chr(com_data[i]) is not '*':
            data.append(chr(com_data[i]))
print 'result:',data

file_object = open('file.txt','a+')
try:
    file_object.write(str(data)+'\n')
finally:
    file_object.close()
print '读射频卡结果：',result



