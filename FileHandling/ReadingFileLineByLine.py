#Reading a file line by line using loop

obj=open("file1.txt","r");

for i in obj:    # obj stores a whole file as list and each line as an item(string)
    print(i);