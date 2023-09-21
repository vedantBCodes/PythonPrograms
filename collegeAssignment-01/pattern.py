"""
print the following pattern

?
# #
? ? ?
# # # #
? ? ? ? ?

"""
for i in range(1,6):
    for j in range(0,i):
        if(i%2==1):
            print("? ",end=" ");
        else:
            print("# ",end=" ");
    print();