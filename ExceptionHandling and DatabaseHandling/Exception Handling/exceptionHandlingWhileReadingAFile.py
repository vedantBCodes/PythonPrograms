try:
    obj=open("file1.txt","r");
except:
    print("File doesn't exists !");
else:
    data = obj.read();
    print(data);
