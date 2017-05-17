#encoding:utf-8

import threading
from time import ctime
import sys
sys.path.append('/home/pi/project_rfid/smart_project/smart_project/site')
import write
import write_two

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args

    #def getResult(self):
    #    return self.res

    def run(self):
        print 'starting',self.name,'at:',ctime()
        self.res = apply(self.func,self.args)
        print self.name,'finished at:',ctime()

def test_interger():
    set_data = [1 for i in range(16)]
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_int_ch():
    set_data = ['a','b','c','d',1,2,3,4,5,6,7,8,9,0,'a','b']
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_float():
    set_data = ['a','b','c','d',1.00,2.00,3.00,4.00,5.0,6.0,7.0,8.0,9.0,0,'a','b']
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_bool():
    set_data = [True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False]
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_dict():
    set_data = ('a','b','c','d',1.00,2.00,3.00,4.00,5.0,6.0,7.0,8.0,9.0,0,'a','b')
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_character():
    set_data = u'cityio_001-00001'
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_zhcn():
    set_data = u'趣活科技货物1'
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_cityid():
    set_data = '5875d4dc2bf1d0ac79e05fb8'
    result =  write.rfid_write_8(set_data,True)
    result =  write_two.rfid_write_16(set_data,True)
    #print "The result of write into the card：%s " % result.code

def test_shortdata():
    set_data = '123456789'
    result =  write.rfid_write_8(set_data,True)
    print "The result of write into the card：%s " % result.code

funcs = [test_zhcn,test_interger,test_shortdata,test_cityid]


def main():
    nfuncs = range(len(funcs))

    threads = []
    for i in nfuncs:
        t=MyThread(funcs[i],(),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        #print threads[i].getResult()

    print 'all DONE'

if __name__=='__main__':
    #main()
    #test_zhcn()
    #test_cityid()
    test_dict()

