import pymongo

client=pymongo.MongoClient();

db=client["School"];

dbcol=db["Student"];

myQuery={"Name":"Vedant"};

newValues={"$set" :{ "Name":"BVedant"}};

dbcol.update_one(myQuery,newValues);

for x in dbcol.find():
    print(x);