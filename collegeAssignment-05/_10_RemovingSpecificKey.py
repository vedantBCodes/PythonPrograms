studentID={
    'Vedant':123,
    'Rahul':456,
    'Omkar':789,
    'Aditya':321,
}
#Removing a key from the dictionary

key=input("Enter a key you want to remove : ");

check=False;
for i in studentID:
    if(i==key):
        check=True;

if(check==True):
    del studentID[key];
    print(f"Dictionary items after removing {key} key :");
    for i in studentID:
        print(f"{i} : {studentID[i]}");
else:
    print(f"Item with key {key} doesn't exists");


