import read
from read import rfid_read

import errors
import test_write

a = True
result = rfid_read(a)   #执行读操作，看返回结果


print '读射频卡结果：',result.code_name



