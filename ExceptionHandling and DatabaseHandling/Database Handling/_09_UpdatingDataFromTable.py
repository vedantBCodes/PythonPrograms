#Updating data into tables

import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_Cursor=my_db.cursor();

query="update studentData set rollNo=%s where name=%s";

#If the database is not set in the connect() method then use database_name.table_name

value=(12,"vedant");

my_Cursor.execute(query,value);

my_db.commit();

print("Data Updated");

#Displaying the updated data

my_Cursor.execute("select * from studentData");

tableData=my_Cursor.fetchall();

for i in tableData:
    print(i);