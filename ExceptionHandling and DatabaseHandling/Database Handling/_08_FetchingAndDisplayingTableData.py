#Fetching data from the table

import  mysql.connector as myconn

my_db=myconn.connect(host="localhost",user="root",password="veda1234");

my_cursor=my_db.cursor();

my_cursor.execute("select * from Student.studentData"); #If we already set the database then only table name is enough

my_record=my_cursor.fetchall(); #fetchall() method fetch all the data from the table

#Now all the record from studentData table ia in the my_record object

#Displaying the data

for i in my_record:
    print(i);