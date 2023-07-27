rollNo=[4,5,3,7,6];
students=["vedant","pratik","omkar"];
mix_list=[1,"vedant",14.25,True];

#Accessing whole list

print(rollNo);
print(students);
print(mix_list);

#Accessing individual items

print(rollNo[0]);
print(rollNo[4]);

#Negative indexing

print(rollNo[-1]);
print(rollNo[-3]);

#List Slicing

print(rollNo[0:4]);
print(rollNo[1:3]);

#Sorting Sort

rollNo.sort()
print(rollNo);
rollNo.reverse()
print(rollNo);

#Finding Maximum and minimum numbers

x=min(rollNo);
print(x);
y=max(rollNo);
print(y);

#Inserting item in a list

rollNo.append(9);
print(rollNo);
rollNo.insert(0,12);
print(rollNo);
rollNo.extend([14,16,20]);
print(rollNo);

#Replacing an item in a list

rollNo[0]=90;
print(rollNo);

#Removing an item in a list

rollNo.remove(90);
print(rollNo);

#Counting occurance of an item

z=rollNo.count(3);
print(z);

#Finding the index of an item

print(rollNo.index(9));

#Deleting a perticular item from a list

rollNo.pop(5);   #Here we are passing index i.e 5 is index here
print(rollNo);