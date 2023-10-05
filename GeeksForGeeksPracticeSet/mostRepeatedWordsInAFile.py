obj=open("file1.txt","r");
str=obj.read();
strList=str.split(" ");
maxCount=0;
for item in strList:
    cnt=strList.count(item);
    if(cnt>maxCount):
        maxCount=cnt;
        MostRepeatedItem=item;

print(f"Most repeated word in a given file is {MostRepeatedItem}");