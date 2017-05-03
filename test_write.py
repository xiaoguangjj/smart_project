#encoding:utf-8

import write
import errors

from write import rfid_write

val = 3

if val == 1:
    set_data = [1 for i in range(16)]
elif val == 2:
    set_data = ['c','i','t','y','i','o','_',0,0,1,'-',0,0,0,0,1]    
elif val == 3:
	#set_data = [u'趣',u'活',u'科',u'技',u'货',u'1']
    set_data = u'趣活科技货1'
elif val == 4:
    set_data = '5875d4dc2bf1d0ac79e05fb8'   #data for test is more long than 16 bits
elif val == 5:
    set_data = [1 for i in range(15)]   #data for test is more short than 16 bits


result =  rfid_write(set_data,start_reading=True)    

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

print "写入射频卡结果：%s " % result.code

