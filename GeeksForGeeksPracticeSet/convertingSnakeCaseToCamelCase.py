str1=input("Enter the snake case string : ");

strList=str1.split("_");

print(strList);

str2="";
cnt1=1;
for i in strList:
    if(cnt1==1):
        str2=str2+i;
        cnt1+=1;
    else:
        cnt2 = 1;
        for j in i:
            if (cnt2 == 1):
                str2 = str2 + j.upper();
                cnt2 += 1;
            else:
                str2 = str2 + j;


print(f"The snakeCase conversion : {str2}");