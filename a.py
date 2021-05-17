import pymongo
import urllib.parse
print("Hello")
username = urllib.parse.quote_plus('Lonecannibal')
password = urllib.parse.quote_plus('P@ssword')
client = pymongo.MongoClient("mongodb://%s:%s@cluster0-shard-00-00.fyo1f.mongodb.net:27017,cluster0-shard-00-01.fyo1f.mongodb.net:27017,cluster0-shard-00-02.fyo1f.mongodb.net:27017/sample_airbnb?ssl=true&replicaSet=atlas-8k0uuk-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = client["mydatabase"]


print(mydb.list_collection_names())