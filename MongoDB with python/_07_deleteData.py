import pymongo

client=pymongo.MongoClient();

db=client["School"];

dbcol=db["Student"];

myQuery={"Name" : "Paris" };

dbcol.delete_one(myQuery);

for x in dbcol.find():
    print(x);