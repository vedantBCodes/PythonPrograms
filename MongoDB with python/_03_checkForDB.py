import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/"); # URL is optional

dbs=client.list_database_names();

dbName="School"

if(dbName in dbs):
    print("Database exists");
else:
    print("Database doesn't exists");

print(f"Listing all databases : {dbs}")