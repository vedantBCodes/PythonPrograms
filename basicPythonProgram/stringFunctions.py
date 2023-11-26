name1=input("Enter your name:");
name2="pratik";

# String function

print(name1.upper());
print(name1.lower());
print(name2.index('a'));

#As strings in python are immutable in nature , above function will not change the original string

print('t' in name2);
x=len(name1);
print(f"The number of characters in {name1} are {x}");

''' As String is a collection of characters 
we can access the characters by providing it's index.
String index starts from zero'''

print("The character at index 2 in {name1} is "+name1[2]);

