from pymongo import MongoClient

class Mongo(object):
    '''
    数据库操作
    '''
    def __init__(self,db_name,card_num):
        client = MongoClient('0.0.0.0',27017)
        #db_name = 'RFID_card'
        db = client[db_name]
        #card_s = db['card_num']
        card_s = db[card_num]
    def del_db(self,db):
        db.card_s.drop()
    def insert_db(self,db,uid,num,data):
        u = dict(name=uid,chunk=num,num=data)
        db.card_s.insert(u)

