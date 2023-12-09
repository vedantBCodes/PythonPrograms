import myPackage.myStringMethods as myString

"""
One can also import the package like this -->from myPackage import myStringMethods as myString
"""

str1="vedant";
str2=myString.stringReverse(str1);

print(f"The reversed string : {str2}");

str3="madam";

if(myString.stringPallindrome(str3)==True):
    print(f"{str3} is a pallindrome string");
else:
    print(f"{str3} is not a pallindrome string");