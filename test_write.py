import write
import errors

from write import rfid_write


set_data = [1 for i in range(16)]
a = True
result =  rfid_write(set_data,a)    #执行写入读卡器操作，看返回结果
'''
def errdatashort():
    return errors.ErrorDataShort().code_name

def errdatalong():
    return errors.ErrorDataLong().code_name

def errwritenotfind():
    return errors.ErrorWriteNotFind().code_name

def errwritefailedunkown():
    return errors.ErrorWriteFailedUnkown().code_name

def errreadnotfind():
    return errors.ErrorReadNotFind().code_name

def errreadfailedunknow():
    return errors.ErrorReadFailedUnknow().code_name

def errscancardfailed():
    return errors.ErrorScanCardFailed().code_name

def errchangedataerr():
    return errors.ErrorChangeDataErr().code_name

def errevaluteerr():
    return errors.ErrorEvaluteErr().code_name

def errAuthenticationErr():
    return errors.ErrorAuthenticationErr().code_name


choice = {'40101':errdatashort,'40102':errdatalong,'40103':errwritenotfind,'40104':errwritefailedunkown,'40105':errreadnotfind,'40106':errreadfailedunknow,'40107':errscancardfailed,'40108':errchangedataerr,'40109':errevaluteerr,'40110':errAuthenticationErr}


def find(num):
    choice.get(num)()
'''

print '写入射频卡结果：',result.code_name

