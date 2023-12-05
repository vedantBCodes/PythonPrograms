#Establishing connection between MySQL and Python

import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="veda1234");

#Here mydb is an object
#connect() is a method of connector class with some parameters

print(mydb);
print("Connection Established Successfully");