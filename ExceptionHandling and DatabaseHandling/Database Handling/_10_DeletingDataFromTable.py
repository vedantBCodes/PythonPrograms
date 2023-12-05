#Deleting data from table

import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor=my_db.cursor();

query="delete from studentData where name=%s";
value=("vedant",);

my_cursor.execute(query,value);

my_db.commit();

print("Data deleted !");

my_cursor.execute("select * from studentData");

record=my_cursor.fetchall();

for i in record:
    print(i);