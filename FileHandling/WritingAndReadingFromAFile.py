obj=open("file1.txt","w+");
msg=input("Enter a new message : ");  # This message will override the previous data
obj.write(msg);
data=obj.read();
print(data);
obj.close()