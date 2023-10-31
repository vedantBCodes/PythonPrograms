
def toUppercase(str1):
    emptyStr="";
    for i in range(0,len(str1)):
        emptyStr=emptyStr+str1[i].upper();
    return emptyStr;

def toLowercase(str1):
    emptyStr="";
    for i in range(0,len(str1)):
        emptyStr=emptyStr+str1[i].lower();
    return emptyStr;

str1="veant";
upperStr=toUppercase(str1);
print(f"The uppercase conversion : {upperStr}");

str2="VEDANT";
lowerStr=toLowercase(str2);
print(f"The lowercase conversion : {lowerStr}");
