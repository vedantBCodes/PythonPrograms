#Deleting whole records from table

import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor=my_db.cursor();


my_cursor.execute("truncate table studentData3");

my_db.commit();

print("Whole record deleted!");

my_cursor.execute("select * from studentData3");

# record=my_cursor.fetchall();

for i in my_cursor:
    print(i);