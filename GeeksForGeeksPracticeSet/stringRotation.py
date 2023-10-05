"""
Given a string of size n, write functions to perform following operations on string.

Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n).
Examples:

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe"
         Right Rotation : "ksGeeksforGee"

Input : s = "qwertyu"
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"
"""

def stringRotation(str1,d):
    leftRotatedstring=str1[d:]+str1[0:d];
    rightRotatedstring = str1[-d:] + str1[0:-d];
    print(f"Anticlockwise Rotation  : {leftRotatedstring}");
    print(f"Clockwise Rotation : {rightRotatedstring}");

str1="GeeksforGeeks";
d=2;  #d-no. of rotation
stringRotation(str1,d);