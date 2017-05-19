#!/usr/bin/env python
# -*- coding: utf8 -*-
from pymongo import MongoClient

class Mongo_Op(object):
    '''
    数据库操作
    '''
    def __init__(self,db,db_name,card_num):
        client = MongoClient('0.0.0.0',27017)
        #db_name = 'RFID_card'
        db = client[db_name]
        #card_s = db['card_num']
        card_s = db[card_num]
    def del_db(self,db):
        db.card_s.drop()
    def insert_db(self,db,uid,order,data):
        u = dict(uid=uid,chunk=order,num=data)
        db.card_s.insert(u)
    def find_db(self,db,uid,order):
        db.card_s.find({'uid':uid},{'chunk':order})
    def update_db(self,db,uid,order,data):
        db.card_s.update({'uid':uid,'chunk':order},{'$set':{'num':data}})

