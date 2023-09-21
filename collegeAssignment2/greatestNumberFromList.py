numbers=input("Enter the list elements seperated by spaces : ");

number_list=numbers.split(" ");

count=0;

for i in number_list:
    count=count+1

for i in range(0,count):
    number_list[i]=int(number_list[i]);

max=number_list[0];

for i in range(0,count):
    if(number_list[i]>max):
        max=number_list[i];

print(f"The greatest number from a list is : {max}");