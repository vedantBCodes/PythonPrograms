'''
List comprehension in Python is a concise way to create lists by applying an expression to each item in an iterable
(like a list, tuple, or range). It allows for the creation of a new list by filtering and transforming elements
from an existing iterable in a single line of code.

[expression for item in iterable if condition]

'''
# List comprehension

# Simple List comprehesion

squares=[i**2 for i in range(1,11)];

print(squares);

num=10;

tables=[num*i for i in range(1,11)];

print(tables);

# List comprehesion with a condition

evens = [i for i in range(1,11) if i%2==0];

print(evens);

# List comprehesion with a functions

def square(num):
    return num*num;

squares2 = [square(i) for i in range(10)];

print(squares2);

# Nested List Comprehension (for matrix flattening)

matrix=[[1,2,3],[4,5,6],[7,8,9]];

list1=[num for row in matrix for num in row];

print(list1);
