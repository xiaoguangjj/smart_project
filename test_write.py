import write
import errors

from write import rfid_write


set_data = [1 for i in range(16)]
a = True
result =  rfid_write(set_data,a)    #执行写入读卡器操作，看返回结果

print '写入射频卡结果：',result.code_name

