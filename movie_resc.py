import pymongo

client = pymongo.MongoClient("mongodb+srv://tonynhanvo:2ougHiUbBKAWkCDK@cluster0.yuaggbs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

print(collection.find().limit(5))
