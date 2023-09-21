numbers=input("Enter the list elements seperated by spaces : ");

number_list=numbers.split(" ");

count=0;

for i in number_list:
    count=count+1

for i in range(0,count):
    number_list[i]=int(number_list[i]);

total=1;

for i in range(0,count):
    total=total*number_list[i];

print(f"The multiplication of all the list item is {total}");