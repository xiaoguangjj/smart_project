#!/usr/bin/env python
# -*- coding: utf8 -*-
'''
    Read.py
    ~~~~~~~~~~~~~~~~
    Rfid read ic module.
    :copyright: (c) 2017 by jxg.
'''

import RPi.GPIO as GPIO

import MFRC522

import signal

import errors
import threading

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame,continue_reading):
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate

def read1(u1,key,uid):
    global  result
    start_reading = True
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
            da = []
            de = []
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            de = []
            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                try:
                    data = MIFAREReader.MFRC522_Read(8)
                except IOError:
                    print 'Can not find card or your card is damaged.'
                    result = errors.ErrorReadNotFind()
                except Exception as e:
                    print 'Exception :',e
                    result = errors.ErrorReadFailedUnknow()
                print 'The data after change:'
                asci = set([i for i in range(127)])
                ddata = set(data)
                if ddata.issubset(asci):
                    for i in range(len(data)):
                        de.append(chr(data[i]))
                        #da.append(data[i].decode('utf-8'))
                        #print data[i].decode('utf-8')
                    print de
                else:
                    for i in range(len(data)-2):
                        if i%3==0:
                            #da.append((chr(data[i])+chr(data[i+1])+chr(data[i+2])).decode('utf-8'))
                            print (chr(data[i])+chr(data[i+1])+chr(data[i+2])).decode('utf-8')
                        #print da
                MIFAREReader.MFRC522_StopCrypto1()
            else:
                print "Authentication error"
                result = errors.ErrorAuthenticationErr()
        start_reading = False



def read2(u2,key,uid):
    start_reading = True
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
            da = []
            de = []
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 12, key, uid)
            de = []
            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                try:
                    data = MIFAREReader.MFRC522_Read(12)
                except IOError:
                    print 'Can not find card or your card is damaged.'
                    result = errors.ErrorReadNotFind()
                except Exception as e:
                    print 'Exception :',e
                    result = errors.ErrorReadFailedUnknow()
                print 'The data after change:'
                asci = set([i for i in range(127)])
                ddata = set(data)
                if ddata.issubset(asci):
                    for i in range(len(data)):
                        de.append(chr(data[i]))
                        #da.append(data[i].decode('utf-8'))
                        #print data[i].decode('utf-8')
                    print de
                else:
                    for i in range(len(data)-2):
                        if i%3==0:
                            #da.append((chr(data[i])+chr(data[i+1])+chr(data[i+2])).decode('utf-8'))
                            print (chr(data[i])+chr(data[i+1])+chr(data[i+2])).decode('utf-8')
                        #print da
                MIFAREReader.MFRC522_StopCrypto1()
            else:
                print "Authentication error"
                result = errors.ErrorAuthenticationErr()
        start_reading = False


def rfid_read(start_reading):
    global  result
    # while start_reading:
    #
    #     # Scan for cards
    #     status,TagType = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    #
    #     # If a card is found
    #     if status == MIFAREReader.MI_OK:
    #         print "Card detected"
    #
    #     # Get the UID of the card
    #     status,uid = MIFAREReader.MFRC522_Anticoll()
    #
    #     # If we have the UID, continue
    #     if status == MIFAREReader.MI_OK:
    #
    #         # Print UID
    #         print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    #
    #         # This is the default key for authentication
    #         key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
    #         da = []
    #         de = []
    #         # Select the scanned tag
    #         MIFAREReader.MFRC522_SelectTag(uid)
    #
    #         # Authenticate
    #         #status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
    #         status = read1(MIFAREReader.PICC_AUTHENT1A,key,uid)
    threads = []
    t1 = threading.Thread(target=read1,args=())
    threads.append(t1)
    t2 = threading.Thread(target=read2,args=())
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()


    start_reading = False
    #return  result

