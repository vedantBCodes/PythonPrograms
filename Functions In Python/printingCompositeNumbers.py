# printing Composite Numbers between a range

def compositeNumbers(start,end):
    print(f"Composite numbers between {start} and {end} :");
    for i in range(start,end):
        for j in range(2,i):
            if(i%j==0):
                print(f"{i} ",end="");
                break;

compositeNumbers(1,50);