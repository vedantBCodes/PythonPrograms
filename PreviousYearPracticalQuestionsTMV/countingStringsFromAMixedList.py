#Initializing list items

list1=["ved",123,"ant",321,"vedant"];

cnt=0;
for i in list1:
     if(type(i)==str):
          cnt+=1;

print(f"The number of strings from a given list1 are :{cnt}");

#Taking list items from user
#While taking input of list items all the items are converted into string

list2=input("Enter some strings :").split();

for i in range(len(list2)):
     if((list2[i][0]>='a') and (list2[i][0]<='z') or (list2[i][0]>='A') and (list2[i][0]<='Z')):
           list2[i]=str(list2[i]);
     else:
          list2[i] = int(list2[i]);

cnt=0;
for i in list2:
     if(type(i)==str):
          cnt+=1;

print(f"The number of strings from a given list are2 :{cnt}");

