obj=open("file1.txt","r");

line=int(input("Enter the line number you want to reverse :"));

cnt=1;

data="";
for i in obj:
    if(cnt==line):
        i=i.split();
        i.reverse();
        empty="";
        for j in range(len(i)):
            empty=empty+" "+i[j];
        data=data+empty+"\n";
    else:
        data=data+i;
    cnt+=1;

obj.close();

obj1=open("file1.txt","w+");
obj1.write(data);
obj1.seek(0);
data1=obj1.read();
print(data1);
obj1.close();