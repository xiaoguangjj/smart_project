#!/usr/bin/env python
# -*- coding: utf8 -*-
''' 
    Write.py
    ~~~~~~~~~~~~~~~~
    Rfid write ic module.
    :copyright: (c) 2017 by jxg.
'''

import RPi.GPIO as GPIO
import MFRC522
import signal
import pymongo
import sys
import errors

from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding('utf-8')

client = MongoClient('0.0.0.0',27017)
db_name = 'RFID_card'
db = client[db_name]
collection_card_num = db['card_num']

continue_reading = True

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

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
def deal_data(set_data,data):
    if len(set_data) == 16:
        try:
            data = set_data
        except AttributeError as e:
            print 'Exception:',e
    elif len(set_data) < 16:
        for i in range(0,(16 - len(set_data))):
            set_data.append(0x00)
        result = errors.ErrorDataShort().code
    else:
        for i in range(16):
            data.append(set_data[i])
        return 'please input 16 bits data.'
    print "Now we fill it with 0x00:"

    try:
        MIFAREReader.MFRC522_Write(8, data)
    except IOError:
        print 'Can not find your card or your card is damaged.'
    except Exception as e:
        print 'Exception :',e

    print "It is now empty:"
                    # Check to see if it was written
    try:
        MIFAREReader.MFRC522_Read(8)
    except IOError:
        print 'Can not find your card or your card is damaged'
    except Exception as e:
        print 'Exception :',e
 
def rfid_write(set_data,start_reading):
    while start_reading:
    
        # Scan for cards    
        status,TagType = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

        # Get the UID of the card
        status,uid = MIFAREReader.MFRC522_Anticoll()

       # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:

                data = []
	        # te = []
            #    # Fill the data with 0x00
            #
	        # l = db.collection_card_num.find_one({'name':'card'},{'num':1,'_id':0})
	        # str = l.get('num',0)
	        # #print str.encode('utf-8')
	        # #print len(l.get('num',0))
	        # for i in range(0,len(l.get('num',0))):
	       	#     #data.append(ord(l.get('num',0)[i]))
		    #    data.append(l.get('num',0)[i].encode('utf-8'))
		    #    print l.get('num',0)[i].encode('utf-8')

                deal_data(set_data,data)
                # Stop
                MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
                start_reading = False

            else:
                print "Authentication error"
