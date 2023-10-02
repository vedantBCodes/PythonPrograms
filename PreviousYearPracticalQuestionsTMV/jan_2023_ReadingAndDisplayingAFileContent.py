obj=open("file1.txt");  #OR obj=open("file1.txt","r");    r is a default mode
data=obj.read();
print(data);
obj.close();