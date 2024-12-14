import pymongo

client=pymongo.MongoClient();

db=client["School"];

dbcol=db["Student"];

for x in dbcol.find():
    print(x);