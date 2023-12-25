#Establishing connection between MySQL and Python

import mysql.connector as myconn   #Here mysql is a package and connector is the class defined in that package

mydb=myconn.connect(host="localhost",user="root",password="veda1234"); #connect() ia the method of connector class

#Here mydb is an object
#connect() is a method of connector class with some parameters

print(mydb);
print("Connection Established Successfully");
