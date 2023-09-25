"""Input: 10
Output:
                 *   *
                 *   *
             *   *   *   *
             *   *   *   *
         *   *   *   *   *   *
         *   *   *   *   *   *
     *   *   *   *   *   *   *   *
     *   *   *   *   *   *   *   *
 *   *   *   *   *   *   *   *   *   *
 *   *   *   *   *   *   *   *   *   *

"""

rows=int(input("Enter the even number of rows : "));

if(rows%2==1):
    rows+=1;    #To make double sided stair-case no. of rows must be even

x=(rows-2)/2;
y=x+1;

for i in range(0,rows):
    for j in range(0,rows):
        if(j>=x and j<=y):
            print(" * ",end=" ");
        else:
            print("   ",end=" ");
    if (i%2==1):
        x -= 1;
        y += 1;
    print();

