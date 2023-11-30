#Reading even lines from a file

#Even lines

obj=open("file1.txt","r");

cnt1=1;
for i in obj:
    if(cnt1%2==0):
        print(i,end="");  #to avoid extra line break
    cnt1+=1;

print("\n"); #To add a next line

obj.close();  #Closing a file to move file pointer back to the start

#Reading odd lines from a file

#Odd lines
obj=open("file1.txt","r");

cnt2=1;
for j in obj: #Here the file pointer is at the starting
    if(cnt2%2!=0):
        print(j,end="");
    cnt2+=1;

obj.close();