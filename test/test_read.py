#encoding:utf-8

from site.read import rfid_read
from site.read_two import rfid_read2

#import test_write

#注意s50卡数据块读时需要从后往前读

result = rfid_read2(True)
result = rfid_read(True)

print '读射频卡结果：',result.code_name



