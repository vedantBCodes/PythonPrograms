str1=input("Enter a sentence : ");

str1List=str1.split(" ");

cnt=0;
for i in str1List:
    cnt=cnt+1;

print(f"The total number of strings in a given sentence are : {cnt}");