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
for i in range(len(com_data)):
    if chr(com_data[i]) is not '*':
        data.append(chr(com_data[i]))
print 'result:',data

print '读射频卡结果：',result



