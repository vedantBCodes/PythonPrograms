#Deleting table from database

import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor=my_db.cursor();

my_cursor.execute("drop table studentData2");

my_db.commit();

print("Table deleted!");

my_cursor.execute("show tables");

# record=my_cursor.fetchall();

for i in my_cursor:
    print(i);