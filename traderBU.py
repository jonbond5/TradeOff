from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.tradeoff

traderDB = db.traders
merchDB = db.merchandise

def getUserByField(field, value):
    assert type(field) == str and type(value) == str

    # Will throw exception if not found, intended behavior
    mongoid = traderDB.find({'details.'+field: value})[0]['_id']

    return Trader(mongoid)

class Trader:
    mongoId = None
    details = None

    def __init__(self, args):
        if type(args) == dict:
            self.details = args
            self.mongoId = traderDB.insert_one(self.getDictionary()).inserted_id
        elif type(args) == ObjectId:
            self.details = traderDB.find({"_id": args})[0]['details']
            self.mongoId = args
        else:
            assert False
        

    def getDictionary(self):
        assert self.details != None
        return { 'merch': [], 'wantedmerch': [], 'details': self.details }

    def createMerch(self, merch):
        # Add to db, associate with this trader
        # merch should not currently be in db, merch.mongoId undefined
        # TODO clean up if error is thrown

        assert type(self.mongoId) == ObjectId and merch.mongoId == None

        # Set merch's owner id 
        merch.traderId = self.mongoId
        
        # insert merch with self as it's owner
        result = merchDB.insert_one(merch.getDictionary())

        # Update merch object to reflect state of db
        merch.mongoId = result.inserted_id

        # Add to possession of Trader
        traderDB.update_one(
            { "_id": self.mongoId },
            { "$push": { "merch": merch.mongoId } } 
            )

    def destroyMerch(self, merch):
        # Remove from db, ensure there are not any dangling "pointers"
        # of another user in the other db
        # Specifically, check "wants"

        assert merch.mongoId != None

        # Remove all references to merch
        traderDB.update_many({}, {"$pull": {"merch": merch.mongoId}})

        # Remove all references to merch
        traderDB.update_many({}, {"$pull": {"wantedmerch": merch.mongoId}})

        # Remove merch itself
        merchDB.delete_one({"_id": merch.mongoId})

        # Update merch object to reflect state of db
        merch.traderId = merch.mongoId = None

    def transferMerch(self, merch, other):
        # Moves merch from self to other
        # TODO Check that other wants and self is selling and self possesses

        assert type(self.mongoId)  == ObjectId and \
               type(other.mongoId) == ObjectId and \
               merch.mongoId != None

        # Take from self
        traderDB.update_one({"_id": self.mongoId}, {"$pull": {"merch": merch.mongoId}})

        # Give to other
        traderDB.update_one({"_id": other.mongoId}, {"$push": { "merch": merch.mongoId }})
        
        # Update owner
        merchDB.update_one({"_id": merch.mongoId}, {"$set": { "owner": other.mongoId }})
        merch.traderId = other.mongoId
        
        # Remove from other's wanted
        traderDB.update_one({"_id": other.mongoId}, {"$pull": {"wantedmerch": merch.mongoId}})

    def enumerateMerch(self):
        # Return an iterable that yields this trader's merch
        return self.enumerateArray('merch')


    def enumerateWantedMerch(self):
        # Return an iterable that yields this trader's wanted merch
        return self.enumerateArray('wantedmerch')

    def enumerateArray(self, arrayname):
        assert type(self.mongoId) == ObjectId

        merchids = traderDB.find({"_id": self.mongoId})[0][arrayname]
        merchdetails = merchDB.find({"_id": {"$in": merchids}})

        try:
            while True:
                nxt = merchdetails.next()
                ret = Merchandise(nxt['details'])
                ret.mongoId = nxt['_id']
                ret.traderId = nxt['owner']
                yield ret
        except StopIteration:
            pass


    def addWantedMerch(self, merch):
        # Add merch of another user to merch this user wants
        # Corner cases: (TODO)
        #   Make sure this user does not possess given merch
        #   Make sure this user does not already want this merch
        #   Make sure merch exists
        assert type(self.mongoId) == ObjectId and merch.mongoId != None

        traderDB.update_one(
            { "_id": self.mongoId },
            { "$push": { "wantedmerch": merch.mongoId } } 
            )

    # TODO Make general functions which add to an array within trader, or
    # enumerate an array within a trader?

        

'''
Represents an object that an individual will buy/sell.

Merchandise.name: Name of merchandise

Merchandise.mongoId: MongoDB Identifier for item

Constructor: Pass it a dictionary you want to store and affiliate with this merch.
'''
class Merchandise:
    mongoId = None
    traderId = None
    details = None

    def __init__(self, args):
        if type(args) == dict:
            self.details = args
        elif type(args) == ObjectId:
            self.mongoId = args
            info = merchDB.find({"_id": args})[0]
            traderId = info['owner']
            details = info['details']
        else:
            assert False

    def getDictionary(self):
        assert self.traderId != None and self.details != None
        return {"owner": self.traderId, "details": self.details}

    def getTrader(self):
        assert self.traderId != None
        return Trader(self.traderId)
