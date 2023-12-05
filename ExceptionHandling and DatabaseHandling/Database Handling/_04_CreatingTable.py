#Creating table using python

import mysql.connector as myconn

myDB=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

myCursor=myDB.cursor();

myCursor.execute("create table studentData3 (rollNo int(2),name varchar(10));");

myCursor.execute("create table customers (name varchar(255), address varchar(255))");

print("Table Created Successfully !");