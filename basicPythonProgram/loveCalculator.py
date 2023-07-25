hisName=input("Enter his name:");
herName=input("Enter her name:");
combineName=hisName+herName;
lowerCombineName=combineName.lower();
t=lowerCombineName.count('t');
r=lowerCombineName.count('r');
u=lowerCombineName.count('u');
e=lowerCombineName.count('e');

true=t+r+u+e;

l=lowerCombineName.count('l');
o=lowerCombineName.count('o');
v=lowerCombineName.count('v');
e=lowerCombineName.count('e');

love=l+o+v+e;

trueLove=str(true)+str(love);

print(f"Your love percentage is {trueLove}");