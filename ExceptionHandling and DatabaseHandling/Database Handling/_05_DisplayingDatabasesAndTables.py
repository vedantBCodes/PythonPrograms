import mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234");

my_cursor=my_db.cursor();

my_cursor.execute("show databases");

print("The databases are :");
for i in my_cursor:
    print(i);

my_db2=myconn.connect(host="localhost",user="root",password="veda1234",database="Student");

my_cursor2=my_db2.cursor();

my_cursor2.execute("show tables");

print("The Tables in Student database are :");
for i in my_cursor2:
    print(i);