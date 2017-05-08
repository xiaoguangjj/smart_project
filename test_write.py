#encoding:utf-8

import write
import errors
import threading
from time import sleep,ctime
from write import rfid_write


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
    set_data = [1234567890123456]
    result =  rfid_write(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_character():
    set_data = u'cityio_001-00001'
    result =  rfid_write(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_zhcn():
    set_data = u'趣活科技货1'
    result =  rfid_write(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_cityid():
    set_data = '5875d4dc2bf1d0ac79e05fb8'
    result =  rfid_write(set_data,True)
    print "The result of write into the card：%s " % result.code

def test_shortdata():
    set_data = [123456789]
    result =  rfid_write(set_data,True)
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
    main()
    #test_zhcn()



