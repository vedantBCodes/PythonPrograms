studentMarks={
    'Vedant':80,
    'Rahul':95,
    'Omkar':85,
    'Aditya':90,
    'Pratik':75
}
#Sum of values in a dictionary

#Method -1

total1=sum(studentMarks.values());

print(f"sum of all the values in a given dictionary : {total1}");

#Method -2

total2=0;

for i in studentMarks.values():
    total2=total2+i;

print(f"sum of all the values in a given dictionary : {total2}");