str1=input("Enter the snake case string : ");

strList=str1.split("_");

str2="";
for i in strList:
        cnt2 = 1;
        for j in i:
            if (cnt2 == 1):
                str2 = str2 + j.upper();
                cnt2 += 1;
            else:
                str2 = str2 + j;


print(f"The Camel Case conversion : {str2}");