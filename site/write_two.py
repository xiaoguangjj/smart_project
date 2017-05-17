#!/usr/bin/env python
#encoding:utf-8

'''
    Write.py
    ~~~~~~~~~~~~~~~~
    Rfid write ic module.
    :copyright: (c) 2017 by jxg.
'''

import signal
import sys
import re
import logging

from pymongo import MongoClient

logger = logging.getLogger(__name__)
import RPi.GPIO as GPIO
from vender import MFRC522
import errors

reload(sys)

sys.setdefaultencoding('utf-8')

client = MongoClient('0.0.0.0',27017)
db_name = 'RFID_card'
db = client[db_name]
card_s = db['card_num']

continue_reading = True

class WriteCard(object):
    '''
    写卡功能,将数据写入到磁卡中，然后读出数据
    '''
    def __init__(self,data):
        self.data = data
    def func(self):
        try:
            if self.data:
                MIFAREReader.MFRC522_Write(12, self.data)
            print 'write'
        except IOError:
            print 'Can not find your card or your card is damaged.'
            result = errors.ErrorWriteNotFind()
            logger.debug('===== mss-error: ===== %s',result)

        except Exception as e:
            print 'Exception :',e
            result = errors.ErrorWriteFailedUnkown()

        print "It is now empty:"
            # Check to see if it was written
        try:
            #for i in range((self.i-8)/4):
            if self.data:
                MIFAREReader.MFRC522_Read(12)
        except IOError:
            print 'Can not find your card or your card is damaged'
            result = errors.ErrorReadNotFind()
            logger.debug('===== mss-error: ===== %s',result)

        except Exception as e:
            print 'Exception :',e
            result = errors.ErrorReadFailedUnknow()
            logger.debug('===== mss-error: ===== %s',result)
        #return result

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

"""
str,unicode类型的数据校验
"""
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
def deal_data_str(uid,set_data,data):
    data2 = []
    zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
    match = zhPattern.search(set_data)

    if match:
        print u'有中文: %s'% (match.group(0),)
        #print ord(match.encode('utf-8'))
        for i in range(len(set_data)):
            for j in set_data[i].encode('utf-8'):
                print j,i,type(j)
                data.append(ord(j))
            #print list(set_data)[i].encode('utf-8')
        result = errors.ErrorzhcnErr()
        logger.debug('===== mss-error: ===== %s',result)
    else:
        print u'没有包含中文'

        try:
            if 16<len(set_data)<32:
                for i in range(17,len(set_data)):
                    data.append(ord(set_data[i].encode('utf-8')))
                for i in range(len(set_data),33):
                    data.append(ord('*'))
                print data
            elif len(set_data)==32:
                for i in range(17,32):
                    data.append(ord(set_data[i].encode('utf-8')))
            else:
                pass
        except AttributeError as e:
            print 'Exception:',e
        result = errors.ErrorDataLong()
        logger.debug('===== mss-error: ===== %s',result)
    print "Now we fill it with 0x00:"

    result = WriteCard(data).func()

    #db.collection_card_num.drop()
    u = dict(name=uid,chunk=2,num = data)
    db.card_s.insert(u)
    #if db.card_s.find({'name' : uid},{'chunk' : 2}):
    #    db.card_s.update({'name':uid},{'$set':{'num':data}})
    #else:
    #    db.card_s.insert(u)
    return  result

"""
list,tuple类型的数据校验
"""
def deal_data_list(set_data,data):
    data2 = []
    if len(set_data) == 16:
        try:
            for i in range(16):
                if isinstance(set_data[i],int):
                    data.append(set_data[i])
                else:
                    data.append(ord(set_data[i].encode('utf-8')))
        except AttributeError as e:
            print 'Exception:',e
    elif len(set_data) < 16:
        for i in range(len(set_data)):
            data.append(ord(set_data[i].encode('utf-8')))
        result = errors.ErrorDataShort()
        logger.debug('===== mss-error: ===== %s',result)
    else:
        for i in range(16):
            data.append(ord(set_data[i].encode('utf-8')))
        if len(set_data)<32:
            for i in range(17,(32 - len(set_data))):
                data2.append(ord(set_data[i].encode('utf-8')))
            for i in range(len(set_data),32):
                data2.append(ord('*'))
        elif len(set_data)==32:
            for i in range(17,32):
                data2.append(ord(set_data[i].encode('utf-8')))
        else:
            pass
        result = errors.ErrorDataLong()
        logger.debug('===== mss-error: ===== %s',result)
    print "Now we fill it with 0x00:"

    result = WriteCard(data,data2).func()
    return  result

"""
写入第二块数据，对应s50卡的第12个数据块
"""
def write_second_block(set_data,start_reading):
    #result = 1
    while start_reading:
    
        # Scan for cards    
        status,TagType = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        status,uid = MIFAREReader.MFRC522_Anticoll()
        logger.info('===== log-write-MFRC522_Anticoll: =====')

       # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 12, key, uid)
            logger.info('===== log-write-auth: =====')

            # Check if authenticated
            if status == MIFAREReader.MI_OK :
                data = []

                if isinstance(set_data,str):
                    result = deal_data_str(uid,set_data,data)
                elif isinstance(set_data,list):
                    result = deal_data_list(set_data,data)
                else:
                    result = errors.ErrorparamErr
                    logger.debug('===== mss-error: ===== %s',result)
                # Stop
                MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
                start_reading = False

            else:
                print "Authentication error"
                result = errors.ErrorAuthenticationErr()
                logger.debug('===== mss-not-error: ===== %s',result)

    #return result
