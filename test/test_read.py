#encoding:utf-8

import sys
sys.path.append('/home/pi/project_rfid/smart_project/smart_project/site')

import read
import read_two

#注意s50卡数据块读时需要从后往前读

result = read_two.read_second_block(True)
result = read.read_first_block(True)

print '读射频卡结果：',result.code_name



