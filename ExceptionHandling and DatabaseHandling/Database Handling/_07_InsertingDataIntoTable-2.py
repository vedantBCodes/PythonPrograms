#Inserting multiple rows into a table


import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor=my_db.cursor();

query="insert into studentData(rollNo ,name) values (%s,%s)";

valueList=[
    (22,"Chetan"),
    (23,"Rahul"),
    (24,"Omkar")];

my_cursor.executemany(query,valueList);

my_db.commit();
print("Data inserted successfully :");