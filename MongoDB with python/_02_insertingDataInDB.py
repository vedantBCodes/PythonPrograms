import pymongo  # Importing pymongo driver to access MongoDB database

client = pymongo.MongoClient("mongodb://localhost:27017/"); # Creating MongoClient object and then specifying a connection URL with correct ip address

mydb=client["School"];

mycol=mydb["Student"];  # Here we have created a collection (table) named -> Student and collection object named mycol

data={"Name":"Vedant",
      "Age": 24,
      "Degree":"MCA"}  #Here we have created a document (record) named -> data

mycol.insert_one(data); # Here we are inserting the document(record) into a collection(table)

data2=[{"Name":"Vishwjeet","Age":24,"Degree":"MBBS"},
       {"Name":"Shivtej","Age":21,"Degree":"BTech"},
       {"Name":"Paris","Age":25,"Degree":"MBA"}];

mycol.insert_many(data2); #Here we are inserting many records at the same time
