import pymongo

client=pymongo.MongoClient();

db=client["School"];

collections=db.list_collection_names();

collectionName="Student";

if (collectionName in collections):
    print("Collection exists");
else:
    print("Collection does't exists");

print(f"Listing all collections : {collections}");