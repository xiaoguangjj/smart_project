#!/usr/bin/env python
# -*- coding: utf8 -*-

from flask import *

from pymongo import MongoClient

client = MongoClient('0.0.0.0',27017)
db_name = 'RFID_card'
db = client[db_name]
collection_card_num = db['card_num']

app = Flask(__name__)
card = []

# Scan for cards


@app.route("/",methods=['POST','GET'])

def login():
    error = None
    if request.method == 'POST':
        '''if request.form['username'] != 'admin' or request.form['password'] != '123':
                error= "sorry"
        else:
            return redirect(url_for('index'))'''
        if len(request.form['card_num']) != 16:
            error= "sorry"
        else:
        card = request.form['card_num']
        db.collection_card_num.drop()
        u = dict(name = "card",num = card)
        db.collection_card_num.insert(u)
    ''' u2 = db.collection_card_num.find_one({name:"card"})
	    u2['num'] = card
	    db.collection_card_num.save(u2)'''
    return redirect(url_for('index'))

    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True)
