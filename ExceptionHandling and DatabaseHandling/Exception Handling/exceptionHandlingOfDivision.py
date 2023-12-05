num1=int(input("Enter a number :"));
num2=int(input("Enter another number :"));  #Exception occurs if the num2 is zero

result=0;

try:     #Putting all the risky code inside the try block
    result = num1 / num2;

except:   #Except block will execute if the exception occurs
    print("can't devide by zero");

else:     #else block will only be executed if the except block doesn't execute
    print(result);
finally:  #The finally: block is a place to put any code that must execute, whether the try-block raised an exception or not.
    print("Division");
