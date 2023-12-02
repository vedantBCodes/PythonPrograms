obj=open("file1.txt","r");
data=obj.read();
obj.close();

obj2=open("file1Copy.txt","w");
obj2.write(data);
obj2.close();