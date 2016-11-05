from pymongo import MongoClient

c = MongoClient()
db = c.tradeoffdatabase

def addTrader(user,psk):
    db.traders.insert_one({'user':user,'pass':psk,'give':[],'get':[]})
    return

def addGet(items):
    :

def addGive(items)
