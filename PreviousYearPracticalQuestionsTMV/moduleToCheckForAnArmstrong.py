#Creating a module which contains a class method which check whether the number is armstrong or not

class armstrong:
    total=0;  #Class variable
    def __init__(self,num):   #Parameterized constructor
        tempNum=num;
        while(tempNum>0):
            rem=tempNum%10;
            self.total=self.total+(rem**3);
            tempNum=tempNum//10;
        if(self.total==num):
            print(f"{num} is an amstrong number ");
        else:
            print(f"{num} is not an amstrong number ");
