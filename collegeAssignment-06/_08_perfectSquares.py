
# Perfect squares between 1 and 20

def perfectSquares():
    list1=[];
    for i in range(1,21):
        if(i*i<=20):
            list1.append(i*i);
    print(list1);

perfectSquares();