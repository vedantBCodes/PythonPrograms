#Inserting a single row into a table

import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor=my_db.cursor();

query="insert into studentData(rollNo ,name) values (%s,%s)";

value=(21,"vedant");

my_cursor.execute(query,value);

print("Data inserted successfully :");

my_db.commit();  #To save data