#encoding:utf-8

import read
from read import rfid_read

import errors
#import test_write


result = rfid_read(True)


print '读射频卡结果：',result.code_name



