x=input("Enter a string : ");

length= len(x);
xCopy="";

for i in range(length-1,-1,-1):
    xCopy=xCopy+x[i];

print(f"Reversed string : {xCopy}");