import pymongo
import certifi
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://Arzoo05:T2i4s0h5a@cluster0.l32ka.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test

print(db)

d = {
    "name":"arz",
    "email" : "abc@gmail.com",
    "surname" : "m"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d )
