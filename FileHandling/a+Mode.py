obj=open("file1.txt","a+");
msg=input("Enter a new message : ");  # In a+ mode previous data will not be erased
obj.write(msg);
obj.seek(0);
data=obj.read();
print(data);
obj.close()
