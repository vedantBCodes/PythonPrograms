#Creating a new database using python

import mysql.connector as myconn  #myconn is an alias for mysql.connector

my_db=myconn.connect(host="localhost",user="root",password="veda1234");

db_cursor=my_db.cursor();  #db_cursor is an object

db_cursor.execute("create database Student");  #execute() is a method to run any MySQL query

# "create database Student" is a MySQL query to create a database

print("Database Created Successfully!");