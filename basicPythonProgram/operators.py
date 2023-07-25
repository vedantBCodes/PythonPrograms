#types of operators:

#Arithmetic Operators

print(2+3);   #--->5
print(3-2);   #--->1
print(2*3);   #--->6
print(2**3);  #--->8   ** is an exponant operator 2**3 means 2*2*2
print(5/2);   #--->2.5 (not 2)
print(4/2);   #---->2.0(Always a float value
print(5//2);  #--->2   // is a flow division operator
print(5%2);   #--->1

#Relational Operator

print(5>2);  #--->True
print(2>3);  #---->False
print(5>=2); #--->True
print(3!=4); #--->True
print(2==3); #---->False

#Logical Opearator

print((2>3)and(3>2));  #--->False
print((3>4)or(4>1));  #--->True
print(not(3>4));      #--->True

#Identity Operator  (similar to == operator)

a=5;
b=5;
print(a is b);  #--->True

#Membership Operator

name="Vedant";
print('e' in name);  #--->True
print('x' in name);  #--->False