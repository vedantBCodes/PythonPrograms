obj=open("file1.txt","r+");
data=obj.read();
print(data);
msg=input("Enter a new message : ");  # This message will not erase the previous data
obj.write(msg);
obj.close()