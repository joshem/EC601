import pymongo
import datetime
import operator

myclient = pymongo.MongoClient("mongodv://localhost:27017/")
db = myclient["miniproject3"]
col = db["users"]
col.drop()
