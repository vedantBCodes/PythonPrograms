import pymongo  # Importing pymongo driver to access MongoDB database

client = pymongo.MongoClient("mongodb://localhost:27017/"); # Creating MongoClient object and then specifying a connection URL with correct ip address

mydb=client["School"];  # Here the School is the name of the database and mydb is the database object

# NOTE : In MongoDB database won't be created untill it gets content

# MongoDB waits untill you have created a collection (similar to table) with at least one document (similar to record)

# So here School database won't be created
