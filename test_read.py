#encoding:utf-8

import read
from read import rfid_read
import read_two
from read_two import read2

import errors
#import test_write


result = rfid_read(True)
result = read2()

print '读射频卡结果：',result.code_name



