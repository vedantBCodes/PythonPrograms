obj=open("file1.txt","w+");
msg=input("Enter a new message : ");  # This message will override the previous data
obj.write(msg);
obj.seek(0);
data=obj.read();
print(data);
obj.close()
