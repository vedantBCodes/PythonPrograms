# Largest of any 3 entered integers

# Method -1  (Using max() fucntion)
def maxOf3UsingMax(num1,num2,num3):
    maxNum = max(num1, max(num2, num3));
    return maxNum;

#  Method -2  (Using IF ELSE)

def maxOf3UsingIf(num1,num2,num3):
    if((num1>num2) and (num1>num3)):
            return num1;
    elif(num2>num3):
        return num2;
    else:
        return num3;

x = int(input("Enter 1st number : "));
y = int(input("Enter 2nd number : "));
z = int(input("Enter 3rd number : "));

maxNum=maxOf3UsingMax(x,y,z);

print(f"The largest entered integer is : {maxNum}");

maxNum2=maxOf3UsingIf(x,y,z);

print(f"The largest entered integer is : {maxNum2}");