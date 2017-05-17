#encoding:utf-8

import sys
sys.path.append('/home/pi/project_rfid/smart_project/smart_project/site')

import read
import read_two


#注意s50卡数据块读时需要从后往前读

result = read_two.rfid_read2(True)
result = read.rfid_read(True)

print '读射频卡结果：',result.code_name



