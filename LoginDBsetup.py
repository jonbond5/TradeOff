from pymongo import MongoClient
c = MongoClient()
db = c.Login_DB
posts = db.posts
