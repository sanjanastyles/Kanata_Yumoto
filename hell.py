import pymongo
from pymongo import MongoClient
from pymongo import collection

cluster=MongoClient("mongodb+srv://sharplikekatana:12345@realmcluster.n5awq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=cluster["test"]
collection=db["test"]

post={"_id":0, "name":"walter", "city":"meme"}
collection.insert_one(post)