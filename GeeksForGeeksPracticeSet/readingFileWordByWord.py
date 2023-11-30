obj=open("file1.txt","r");

for line in obj:
    for word in line.split():
         print(word);